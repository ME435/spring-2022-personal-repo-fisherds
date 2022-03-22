classdef BankAccount < handle
    %BANKACCOUNT Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        name
        balance
    end
    
    methods
        function obj = BankAccount(name, balance)
            %BANKACCOUNT Construct an instance of this class
            %   Detailed explanation goes here
            obj.name = name;
            obj.balance = balance;
        end
        
        function withdrawal(obj, amount)
            %METHOD1 Summary of this method goes here
            %   Detailed explanation goes here
            obj.balance = obj.balance - amount;
        end
    end
end

