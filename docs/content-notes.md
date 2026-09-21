# Content and publication notes

## Verified company details (21 September 2026)

- Legal name: blox-it; legal form: Besloten Vennootschap (BV).
- Enterprise number: 0730.696.050; subject to VAT.
- Registered office: Terwestvaart 11, 9180 Lokeren (KBO effective 1 January 2025).
- RPR Gent. The 2021 company deed was filed at the enterprise court of Gent. The site names the court rather than guessing the current division after municipal changes.
- Email and phone retained from the existing company website: info@bloxit.be and +32 485 60 68 40.

Sources:
- KBO Public Search: https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0730696050
- Belgian Official Gazette deed: https://www.ejustice.just.fgov.be/tsv_pdf/2021/04/28/21051418.pdf
- FPS Economy identification requirements: https://economie.fgov.be/nl/themas/online/elektronische-handel/verkoop-internet/bedrijfswebsite-en-accounts-op
- Existing website: https://www.bloxit.be/

The site includes name/legal form, registered office, enterprise/VAT numbers, registry court, email and phone, plus privacy information. No e-commerce checkout, regulated-profession offering, customer accounts or forms are implemented. The privacy text describes this implementation and ordinary email enquiries; review it if tracking, processors or contact handling change.

## Language behaviour

Root homepage is English HTML. If JavaScript is enabled and navigator.language starts with `nl`, the root homepage redirects to `nl/`, preserving the hash. Explicit `?lang=en` prevents automatic selection. EN/NL links work without JavaScript. No cookies, localStorage or sessionStorage are used. Legal pages never automatically redirect.

## Before replacing WordPress

Enable GitHub Pages using GitHub Actions, verify both languages visually on desktop/mobile, then configure the custom domain and DNS. Do not change mail/MX records. Review handling of the old WordPress article URLs before switching the domain: GitHub Pages cannot configure arbitrary HTTP 301 redirects. The new site includes a useful 404 page, not an invented redirect map.

## Validation completed

- Python static build succeeds without third-party dependencies.
- Generated local assets, page links and fragment targets checked; one H1 per page.
- JavaScript language behaviour checked for English, Dutch and unsupported browser languages, explicit choices and project-path/hash preservation.
- Visual browser QA remains pending until Pages is enabled. A failed initial deployment confirms Pages is not yet configured, rather than a build failure.
