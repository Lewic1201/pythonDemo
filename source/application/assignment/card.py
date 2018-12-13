class Card:
    def __init__(self, cardid, password, money):
        self.cardid = cardid
        self.password = password
        self.islock = False
        # 操作记录
        self.operation_history = []
        self.limit_money = 10000 - self.get_limit_money()
        if self.operation_history:
            self.balance = self.operation_history[-1]['balance']
        else:
            self.balance = money
        # money和balance一样
        self.money = self.balance

    def set_change_money(self, change_money, timestamp, flag='b'):
        """ 每次贷款记录到operation_history参数里, flag: b是借,r是还 """
        error_message = ''
        for record in self.operation_history:
            # 过滤重复记录
            if timestamp in record:
                error_message += 'time error or record repeat;'
        a_record = {}
        if error_message == '':
            a_record['timestamp'] = timestamp
            if flag == 'b':
                # 贷款
                a_record['borrow'] = change_money
                a_record['refund'] = 0
                if self.operation_history:
                    # 第二次之后,获取和上一次间隔时间,贷款时间*利率*当前金额
                    a_record['balance'] = (self.balance - change_money) * (
                            1 + 0.0005 * (timestamp - self.operation_history[-1]['timestamp']))
                else:
                    # 第一次记录
                    a_record['balance'] = -change_money
            elif flag == 'r':
                # 还款
                a_record['borrow'] = 0
                a_record['refund'] = change_money
                a_record['balance'] = self.balance + change_money
                if self.operation_history:
                    # 第二次之后,获取和上一次间隔时间,贷款时间*利率*当前金额
                    a_record['balance'] = self.get_balance(timestamp) + change_money
                else:
                    # 第一次记录
                    a_record['balance'] = change_money
            else:
                error_message += 'flag error;'

            self.balance = a_record['balance']
            self.money = self.balance
            self.operation_history.append(a_record)
            print('-' * 50)

    def get_limit_money(self):
        """获取贷款钱数"""
        sum_borrow_money = 0
        for record in self.operation_history:
            sum_borrow_money += record.get('modify_money', 0)
            sum_borrow_money -= record.get('refund', 0)
        return sum_borrow_money

    def get_balance(self, timestamp):
        if self.operation_history:
            return self.balance * (1 + 0.0005 * (timestamp - self.operation_history[-1]['timestamp']))
        else:
            return 0

    def get_last_timestamp(self):
        if self.operation_history:
            return self.operation_history[-1]['timestamp']
        else:
            return 0
