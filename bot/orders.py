from bot.logging_config import setupLogger

logger = setupLogger()

def place_market_order(client, symbol, side, qty):

    try:
        logger.info(f"API Request for Market order | {symbol} | {side} | Quantity: {qty}")
        response =  client.place_order(
            category = "linear",
            symbol=symbol,
            side=side,
            orderType = "Market",
            qty=qty
        )
        logger.info(f"API Response: {response}")
        return response
    except Exception as e:
        logger.error(f"API Request Error: {e}")


def place_limit_order(client,symbol,side,qty,price):

    try:
        logger.info(f"API Request for Limit order | {symbol} | {side} | Quantity: {qty} | Price: {price}")
        response =   client.place_order(
            category = "linear",
            symbol=symbol,
            side = side,
            orderType = "Limit",
            qty=qty,
            price=price,
            timeInForce = "GTC"
        )
        logger.info(f"API Response: {response}")
        return response
    except Exception as e:
        logger.error(f"API Request Error: {e}")

def place_stop_limit_order(client,symbol,side,qty,price,stopPrice):
    trigger_direction = 1 if price > stopPrice else 2
    try:
        logger.info(f"API Request for Stop_Limit order | {symbol} | {side} | Quantity: {qty} | Price: {price} | Stop_Price: {stopPrice}")
        response = client.place_order(
            category = "linear",
            symbol= symbol,
            side= side,
            orderType="Limit",
            qty = qty,
            price=price,
            triggerPrice = stopPrice,
            triggerDirection= trigger_direction,
            timeInForce = "GTC"
        )
        logger.info(f"API Response: {response}")
        return response
    except Exception as e:
        logger.error(f"API Request Error: {e}")
        
