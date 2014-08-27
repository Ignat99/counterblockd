# -*- coding: utf-8 -*-
VERSION = "1.5.0" #should keep up with the counterwallet version it works with (for now at least)

DB_VERSION = 22 #a db version increment will cause counterblockd to rebuild its database off of counterpartyd 

CAUGHT_UP = False #atomic state variable, set to True when counterpartyd AND counterblockd are caught up

UNIT = 100000000

SUBDIR_ASSET_IMAGES = "asset_img" #goes under the data dir and stores retrieved asset images
SUBDIR_FEED_IMAGES = "feed_img" #goes under the data dir and stores retrieved feed images

MARKET_PRICE_DERIVE_NUM_POINTS = 8 #number of last trades over which to derive the market price (via WVAP)

# FROM counterpartyd
# NOTE: These constants must match those in counterpartyd/lib/config.py
REGULAR_DUST_SIZE = 5430
MULTISIG_DUST_SIZE = 5430 * 2
ORDER_BTC_DUST_LIMIT_CUTOFF = MULTISIG_DUST_SIZE
MIN_FEE = 20000
DEFAULT_FEE_PER_KB = 10000

mongo_db = None #will be set on server init

BTC = 'BTC'
XCP = 'XCP'

MAX_REORG_NUM_BLOCKS = 10 #max reorg we'd likely ever see

ARMORY_UTXSVR_PORT_MAINNET = 6590
ARMORY_UTXSVR_PORT_TESTNET = 6591

DEFAULT_COUNTERPARTYD_RPC_PORT = 4000
DEFAULT_COUNTERPARTYD_RPC_PORT_TESTNET = 14000

DEFAULT_BACKEND_RPC_PORT = 8333
DEFAULT_BACKEND_RPC_PORT_TESTNET = 18333

AUTOBTCESCROW_ADDRESS_POOL_MAX_SIZE = 100
AUTOBTCESCROW_NUM_BLOCKS_FOR_BTCPAY = 1 #number of blocks after a valid order match to make a BTCpay
MIN_CONF_FOR_ESCROWED_FUND = 0

# private key should be in bitcoind wallet
ESCROW_COMMISSION_ADDRESS_TESTNET = 'mrssHos2Fn4WKv3PdoXP6A687DG8nd7DTf' 
ESCROW_COMMISSION_ADDRESS = '19U6MmLLumsqxXSBMB5FgYXbezgXYC6Gpe'
ESCROW_COMMISSION = 0.005
BTCPAY_FEE_RETAINER = 100000;

QUOTE_ASSETS = ['BTC', 'XBTC', 'XCP'] # define the priority for quote asset
MARKET_LIST_QUOTE_ASSETS = ['XCP', 'XBTC', 'BTC'] # define the order in the market list


