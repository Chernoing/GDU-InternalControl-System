# 风险预警基础规则匹配逻辑
def check_risk(amount):
    if amount > 10000:
        return "警告：大额交易风险！"
    return "正常交易"