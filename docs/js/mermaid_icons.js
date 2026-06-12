document$.subscribe(async () => {
  const mermaid = await import("https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs")

  const base =
    document.querySelector("base")?.href ??
    `${window.location.origin}/portfolio/`

  const awsIconsUrl = new URL("assets/mermaid-icons/aws-icons.json", base).toString()
  const logosIconsUrl = new URL("assets/mermaid-icons/logos.json", base).toString()

  const [awsIcons, logosIcons] = await Promise.all([
    fetch(awsIconsUrl).then((res) => {
      if (!res.ok) throw new Error(`Cannot load AWS icon pack: ${res.status} ${awsIconsUrl}`)
      return res.json()
    }),
    fetch(logosIconsUrl).then((res) => {
      if (!res.ok) throw new Error(`Cannot load logos icon pack: ${res.status} ${logosIconsUrl}`)
      return res.json()
    })
  ])

  mermaid.registerIconPacks([
    {
      name: "aws",
      icons: awsIcons
    },
    {
      name: "logos",
      icons: logosIcons
    }
  ])

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose",
    theme: document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "default"
  })

  const diagrams = document.querySelectorAll("pre.mermaid-custom > code, code.mermaid-custom")

  for (const [index, code] of diagrams.entries()) {
    const source = code.textContent.trim()
    const wrapper = document.createElement("div")
    wrapper.className = "mermaid"
    wrapper.id = `mermaid-custom-${Date.now()}-${index}`

    code.parentElement.replaceWith(wrapper)

    const { svg } = await mermaid.render(wrapper.id + "-svg", source)
    wrapper.innerHTML = svg
  }
})