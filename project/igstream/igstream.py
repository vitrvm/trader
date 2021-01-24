import time
import sys
import traceback
import logging

from trading_ig import IGService, IGStreamService
from trading_ig.config import config
from trading_ig.lightstreamer import Subscription

# A simple function acting as a Subscription listener
def on_prices_update(item_update):
    # print("price: %s " % item_update)
    print(item_update)

def main():
    logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.DEBUG)

    ig_service = IGService(
        config.username, config.password, config.api_key, config.acc_type
    )

    ig_stream_service = IGStreamService(ig_service)
    ig_session = ig_stream_service.create_session()
    # Ensure configured account is selected
    accounts = ig_session[u"accounts"]
    for account in accounts:
        if account[u"accountId"] == config.acc_number:
            accountId = account[u"accountId"]
            break
        else:
            print("Account not found: {0}".format(config.acc_number))
            accountId = None
    ig_stream_service.connect(accountId)

    # Making a new Subscription in MERGE mode
    subscription_prices = Subscription(
        mode="MERGE",
        items=["CHART:CS.D.GBPUSD.CFD.IP:1MINUTE", "CHART:CS.D.USDJPY.CFD.IP:1MINUTE"],
        fields=["LTV","TTV","UTM","DAY_OPEN_MID","DAY_NET_CHG_MID","DAY_PERC_CHG_MID","DAY_HIGH","DAY_LOW","OFR_OPEN","OFR_HIGH","OFR_LOW","OFR_CLOSE","BID_OPEN","BID_HIGH","BID_LOW","BID_CLOSE","LTP_OPEN","LTP_HIGH","LTP_LOW","LTP_CLOSE","CONS_END","CONS_TICK_COUNT"],
    )
    # adapter="QUOTE_ADAPTER")

    # Adding the "on_price_update" function to Subscription
    subscription_prices.addlistener(on_prices_update)

    # Registering the Subscription
    sub_key_prices = ig_stream_service.ls_client.subscribe(subscription_prices)

    input(
        "{0:-^80}\n".format(
            "HIT CR TO UNSUBSCRIBE AND DISCONNECT FROM \
    LIGHTSTREAMER"
        )
    )

    # Disconnecting
    ig_stream_service.disconnect()


if __name__ == "__main__":
    main()