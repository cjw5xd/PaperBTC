PaperBTC generates a valid Bitcoin address along with its key pair and public
key hash. This can be run on a computer which is not connected to the Internet
to create Bitcoin paper wallets.


SETUP AND EXECUTION
-------------------

Create a virtual environment and install the dependencies:

  virtualenv -p python3 venv
  source venv/bin/activate
  pip install -r requirements.txt

Execute the script:

  python paperbtc.py
