import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def repl(match):
    full = match.group(0)
    src = match.group(1)
    if src.endswith('_low.jpg') or src.startswith('http'): 
        return full
    low_src = re.sub(r'\.(png|jpe?g)$', '_low.jpg', src, flags=re.IGNORECASE)
    return f'data-highres="{src}" src="{low_src}"'

# Match src="something.png" or "something.jpg"
new_html = re.sub(r'src="([^"]+\.(?:png|jpe?g))"', repl, html, flags=re.IGNORECASE)

script = """
  <!-- Adaptive Image Loading based on Network Speed -->
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      const conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
      
      // Check if network is fast (4g) and user hasn't enabled Data Saver
      const isFast = !conn || (!conn.saveData && conn.effectiveType === '4g');
      
      if (isFast) {
        console.log("Fast network (4G) detected: upgrading to high-res images...");
        document.querySelectorAll('img[data-highres]').forEach(img => {
          const highRes = img.getAttribute('data-highres');
          // Smooth preload
          const tempImg = new Image();
          tempImg.onload = () => { img.src = highRes; };
          tempImg.src = highRes;
        });
      } else {
        console.log("Slow network detected (" + (conn ? conn.effectiveType : 'unknown') + "): keeping lightweight compressed images.");
      }
    });
  </script>
</body>
"""

if "Adaptive Image Loading based on Network Speed" not in new_html:
    new_html = new_html.replace('</body>', script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("HTML_UPDATED")
