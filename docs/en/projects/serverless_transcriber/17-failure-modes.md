# Failure Modes

## Lambda execution timeout vs long-running transcription

Third-party transcription can run longer than a single Lambda invocation allows. Submitting audio and waiting synchronously for the transcript inside one Lambda would time out.

**Mitigation:** Decouple submission from result retrieval - the client uploads audio, Lambda submits to AssemblyAI with a webhook URL, and a separate webhook handler fetches the completed transcript when AssemblyAI calls back. The UI polls `GET /jobs` until status becomes `READY`.

## AssemblyAI API errors

If AssemblyAI rejects or fails a request (HTTP 4xx/5xx), the job record is updated to `ERROR` and the failure reason is logged.
