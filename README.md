# efficient-stored-procedure-implementation
database operation where a stored procedure implementation would be more efficient (faster) than doing the same operation by calling SQL queries from an application
"""
Every time we pass a query string to SQL Server the code has to be compiled etc, stored procedures are already compiled and 
ready to run on the server.
 
Also we are sending less data over the network although this is generally a minimal impact anyway.
 
Stored procedures have other benefits.
 
1) Security - Since the actual query is stored on the server we are not transmitting this over the network which means anyone 
intercepting wer network traffic does not gain any insight into wer table structure. Also a well designed SP will prevent 
injection attacks.
 
2) Code seperation, we keep wer database code in wer database and wer application code in wer application, there is very 
little crossover and I find this makes bug fixing a lot nicer.
 
3) Maintainability and Code Reuse, we can reuse a procedure many times without having to copy paste the query, also if we wish 
to update the query we just have to update it in one place.
 
4) Decreased network traffic. As mentioned above this may not be an issue for most people but with a large application we can 
significantly reduce the ammount of data being transferred via wer network by switching to using stored procedures.
"""
