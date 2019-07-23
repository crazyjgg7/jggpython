INSERT INTO  CDRDetail(
            Step,      --没用
            port,      --分机号
	    State,     --状态也没用         
            Reason,    --可能标识来电或者去电
	    CallerDN,  --被叫号码 
	    CalledDN,  --主叫号码
            AgentID,   --分机号
            BinTime,   --起始时间
            EndTime,   --结束时间
            HoldLong,  --通话时间
            RecFile,   --录音文件路径
 
            LogID      --日志ID，可能拿来对应另外一张表用暂时没用                       
        )SELECT
            1, 
            46,
            2,  
            2,
            8999,
            013456698278,
            8999,
            '2019-07-23 15:53:49.000',
            '2019-07-23 15:57:31.000',
            66,
            '20190723\155349.045.wav',
        
            (select max(LogID) from CDRDetail)+1;
