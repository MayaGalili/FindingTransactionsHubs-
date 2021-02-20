class FeaturesNames:
    ORDER_ID = 'order_id'

    ORDER_TOTAL_SPENT = 'order_total_spent'
    BROWSER_IP_INT = 'browser_ip_int'
    EMAIL_INT = 'email_int'
    SHIPPING_ZIP = 'shipping_zip'
    NORMALIZED_FULL_SHIPPING_NAME_INT = 'normalized_full_shipping_name_int'
    ORDER_CAPTURED_AT_INT = 'order_captured_at_int'
    SHIPPING_ADDRESS1_INT = 'shipping_address1_int'

    ORDER_CAPTURED_AT_STR = 'order_captured_at'
    BROWSER_IP_STR = 'browser_ip'
    SHIPPING_ADDRESS1_STR = 'shipping_address1'
    EMAIL_STR = 'email'

    ORDER_STATUS_STR = 'order_status'
    ORDER_STATUS_INT = 'order_status_int'

    # UA_BROWSER_STR = 'ua_browser'
    # UA_BROWSER_INT = 'ua_browser_int'

    NORM_NAME_STR = 'normalized_full_shipping_name'
    NORM_NAME_INT = 'normalized_full_shipping_name_int'

    # COOKIE_STR = 'cookie'
    # COOKIE_INT = 'cookie_int'

    NORMALIZED_FULL_SHIPPING_NAME_STR = 'normalized_full_shipping_name'

    COMBINED = 'combined'


SELECTED_FEATURES = [FeaturesNames.ORDER_TOTAL_SPENT,
                     FeaturesNames.BROWSER_IP_INT,
                     FeaturesNames.EMAIL_INT,
                     FeaturesNames.SHIPPING_ZIP,
                     FeaturesNames.NORMALIZED_FULL_SHIPPING_NAME_INT,
                     FeaturesNames.ORDER_CAPTURED_AT_INT,
                     FeaturesNames.SHIPPING_ADDRESS1_INT,
                     FeaturesNames.ORDER_STATUS_INT]