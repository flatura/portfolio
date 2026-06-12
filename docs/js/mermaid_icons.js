document$.subscribe(async () => {
  const mermaid = await import("https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs")

  const base =
    document.querySelector("base")?.href ??
    `${window.location.origin}/portfolio/`

  const awsIconsUrl = new URL("assets/mermaid-icons/aws-icons.json", base).toString()
  const logosIconsUrl = new URL("assets/mermaid-icons/logos-icons.json", base).toString()

  mermaid.registerIconPacks([
    {
      name: "aws",
      loader: () => fetch(awsIconsUrl).then((res) => res.json())
    },
    {
      name: "logos",
      loader: () => fetch(logosIconsUrl).then((res) => res.json())
    }
  ])

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose"
  })

  document.querySelectorAll(".mermaid[data-processed]").forEach((el) => {
    el.removeAttribute("data-processed")
  })

  await mermaid.run({
    querySelector: ".mermaid"
  })
})