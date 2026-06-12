document$.subscribe(async () => {
  const mermaid = await import("https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs")

  const base =
    document.querySelector("base")?.href ??
    `${window.location.origin}/portfolio/`

  const awsIconsUrl = new URL("assets/aws/aws-icons-mermaid.json", base).toString()

  mermaid.registerIconPacks([
    {
      name: "aws",
      loader: () => fetch(awsIconsUrl).then((res) => res.json())
    }
  ])

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose"
  })

  await mermaid.run({
    querySelector: ".mermaid"
  })
})