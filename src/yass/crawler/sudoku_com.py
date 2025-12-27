from playwright.sync_api import sync_playwright, TimeoutError
import time
import base64

class SudokuComCrawler:
    def __enter__(self):
        self._pw = sync_playwright().start()
        self.browser = self._pw.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.set_default_timeout(10000)
        return self

    def __exit__(self, exc_type, exc, tb):
        self.browser.close()
        self._pw.stop()

    def load(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")
        self.accept_cookies_if_present()

    def screenshot_board(self, path: str = "sudoku.png"):
        for _ in range(20):
            data_url = self.page.evaluate("""
                () => {
                    const canvases = Array.from(document.querySelectorAll('canvas'));
                    if (!canvases.length) return null;
                    const c = canvases.reduce((a,b) => (a.width*a.height) > (b.width*b.height) ? a : b);
                    if (!c) return null;
                    const ctx = c.getContext('2d');
                    if (!ctx) return null;
                    const pixels = ctx.getImageData(0,0,c.width,c.height).data;
                    if (!pixels.some(v => v !== 0)) return null;
                    return c.toDataURL();
                }
            """)
            if data_url:
                break
            time.sleep(0.5)
        else:
            raise RuntimeError("No se pudo capturar el canvas del sudoku")

        header, encoded = data_url.split(",", 1)
        with open(path, "wb") as f:
            f.write(base64.b64decode(encoded))
        print(f"[OK] Screenshot guardado en {path}")

    def accept_cookies_if_present(self):
        try:
            button = self.page.wait_for_selector("#onetrust-accept-btn-handler", timeout=3000)
            button.scroll_into_view_if_needed()
            button.click()
            time.sleep(1)
        except TimeoutError:
            pass
