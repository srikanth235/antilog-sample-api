# antilog-sample-api

A tiny greeting API (Python 3.11+, Flask, pytest) used as a fixture for end-to-end tests of Antilog cloud sessions.

```bash
pip install -r requirements.txt
GREETING=Hello pytest
GREETING=Hello flask --app app run
```

It needs the `GREETING` environment variable (see `.env.example`): a session's environment should set it.

## Tasks for an agent

1. **Feature request.** Add `GET /hello/<lang>` that greets in `en`, `es` or `fr` ("Hello", "Hola", "Bonjour"), returning 404 with `{"error": "unknown language"}` otherwise, with tests.
2. **Use both repos.** With `antilog-sample-web` attached too, document in this README how the web app could call `/hello`.
