import wget

# List of PDF URLs (replace these with your real ones)
pdf_urls = [
    "https://peraturan.bpk.go.id/lib/pdfjs-express-viewer/public/ui/index.html#...1.pdf",
    "https://peraturan.bpk.go.id/lib/pdfjs-express-viewer/public/ui/index.html#...2.pdf",
    "https://peraturan.bpk.go.id/lib/pdfjs-express-viewer/public/ui/index.html#...3.pdf",
]

# Loop and download
for url in pdf_urls:
    try:
        print(f"⬇️ Downloading: {url}")
        filename = wget.download(url)
        print(f"\n✅ Saved as: {filename}\n")
    except Exception as e:
        print(f"❌ Failed to download: {url}", e)