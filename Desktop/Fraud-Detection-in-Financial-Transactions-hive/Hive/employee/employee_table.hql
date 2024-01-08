create database if not exists testdb;
use fraudb;
CREATE TABLE IF NOT EXISTS your_database.your_table (
    account_history ARRAY<STRING>,
    behavioral_patterns STRUCT<avg_transaction_value: DOUBLE>,
    customer_id STRING,
    demographics STRUCT<age: INT, location: STRING>
);
row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/user/hive/warehouse/fraudb.db/employee';