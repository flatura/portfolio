console.log("[mermaid-icons] script file loaded")

;(async () => {
  const LOG_PREFIX = "[mermaid-icons]"

  function log(...args) {
    console.log(LOG_PREFIX, ...args)
  }

  function warn(...args) {
    console.warn(LOG_PREFIX, ...args)
  }

  function error(...args) {
    console.error(LOG_PREFIX, ...args)
  }

  async function fetchJson(url, label) {
    log(`loading ${label}:`, url)

    const response = await fetch(url)

    log(`${label} response status:`, response.status, response.statusText)

    if (!response.ok) {
      throw new Error(`${label} failed: ${response.status} ${response.statusText} ${url}`)
    }

    const json = await response.json()

    log(`${label} loaded`)
    log(`${label} prefix:`, json.prefix)
    log(`${label} icons count:`, json.icons ? Object.keys(json.icons).length : "NO icons FIELD")

    return json
  }

  async function renderMermaidBlocks() {
    log("renderMermaidBlocks started")

    if (typeof document$ === "undefined") {
      warn("document$ is undefined. Running once on current document.")
    } else {
      log("document$ is available")
    }

    log("current location:", window.location.href)

    const base =
      document.querySelector("base")?.href ??
      `${window.location.origin}/portfolio/`

    log("base:", base)

    const awsIconsUrl = new URL("assets/mermaid-icons/aws-icons.json", base).toString()
    const logosIconsUrl = new URL("assets/mermaid-icons/logos.json", base).toString()

    log("awsIconsUrl:", awsIconsUrl)
    log("logosIconsUrl:", logosIconsUrl)

    let mermaid

    try {
      log("importing Mermaid")
      mermaid = await import("https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs")
      log("Mermaid imported:", mermaid)
      log("Mermaid version:", mermaid.default?.version ?? mermaid.version ?? "unknown")
    } catch (e) {
      error("Mermaid import failed", e)
      return
    }

    const mermaidApi = mermaid.default ?? mermaid

    let awsIcons
    let logosIcons

    try {
      ;[awsIcons, logosIcons] = await Promise.all([
        fetchJson(awsIconsUrl, "AWS icon pack"),
        fetchJson(logosIconsUrl, "Logos icon pack")
      ])
    } catch (e) {
      error("Icon pack loading failed", e)
      return
    }

    try {
      log("checking required icon keys")
      log("aws:lambda", !!awsIcons.icons?.lambda)
      log("aws:dynamodb", !!awsIcons.icons?.dynamodb)
      log("aws:api-gateway", !!awsIcons.icons?.["api-gateway"])
      log("aws:simple-storage-service", !!awsIcons.icons?.["simple-storage-service"])
      log("aws:s3", !!awsIcons.icons?.s3)
      log("aws:cognito", !!awsIcons.icons?.cognito)
      log("aws:cloudfront", !!awsIcons.icons?.cloudfront)
      log("logos:chrome", !!logosIcons.icons?.chrome)
      log("logos:webhooks", !!logosIcons.icons?.webhooks)
    } catch (e) {
      error("Icon key check failed", e)
    }

    try {
      log("registering icon packs")

      mermaidApi.registerIconPacks([
        {
          name: "aws",
          icons: awsIcons
        },
        {
          name: "logos",
          icons: logosIcons
        }
      ])

      log("icon packs registered")
    } catch (e) {
      error("registerIconPacks failed", e)
      return
    }

    try {
      log("initializing Mermaid")

      mermaidApi.initialize({
        startOnLoad: false,
        securityLevel: "loose",
        theme: document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "default"
      })

      log("Mermaid initialized")
    } catch (e) {
      error("Mermaid initialize failed", e)
      return
    }

    const blocks = Array.from(document.querySelectorAll(".mermaid-custom"))

    log("found .mermaid-custom blocks:", blocks.length)

    if (blocks.length === 0) {
      warn("No .mermaid-custom blocks found. Check mkdocs.yml custom_fences class.")
      return
    }

    for (const [index, block] of blocks.entries()) {
      log(`processing block #${index}`)
      log(`block #${index} tag:`, block.tagName)
      log(`block #${index} class:`, block.className)

      const source = block.textContent.trim()

      log(`block #${index} source length:`, source.length)
      log(`block #${index} source preview:`, source.slice(0, 200))

      if (!source) {
        warn(`block #${index} is empty, skipping`)
        continue
      }

      const wrapper = document.createElement("div")
      wrapper.className = "mermaid"
      wrapper.id = `mermaid-custom-${Date.now()}-${index}`

      const replaceTarget =
        block.tagName === "CODE" && block.parentElement?.tagName === "PRE"
          ? block.parentElement
          : block

      log(`block #${index} replace target:`, replaceTarget.tagName, replaceTarget.className)

      replaceTarget.replaceWith(wrapper)

      try {
        log(`rendering block #${index}`)

        const renderId = `${wrapper.id}-svg`
        const result = await mermaidApi.render(renderId, source)

        wrapper.innerHTML = result.svg

        log(`block #${index} rendered successfully`)
      } catch (e) {
        error(`block #${index} render failed`, e)
        error(`block #${index} failed source:`, source)

        wrapper.innerHTML = `
          <pre class="mermaid-error">
Mermaid render failed.

${String(e)}

Source:

${source.replace(/[<>&]/g, (ch) => {
  if (ch === "<") return "&lt;"
  if (ch === ">") return "&gt;"
  return "&amp;"
})}
          </pre>
        `
      }
    }

    log("renderMermaidBlocks finished")
  }

  if (typeof document$ !== "undefined") {
    console.log("[mermaid-icons] subscribing to Material document$ lifecycle")

    document$.subscribe(() => {
      console.log("[mermaid-icons] document$ event fired")
      renderMermaidBlocks().catch((e) => {
        console.error("[mermaid-icons] unhandled renderMermaidBlocks error", e)
      })
    })
  } else {
    console.log("[mermaid-icons] document$ unavailable, using DOMContentLoaded fallback")

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", () => {
        renderMermaidBlocks().catch((e) => {
          console.error("[mermaid-icons] unhandled renderMermaidBlocks error", e)
        })
      })
    } else {
      renderMermaidBlocks().catch((e) => {
        console.error("[mermaid-icons] unhandled renderMermaidBlocks error", e)
      })
    }
  }
})()