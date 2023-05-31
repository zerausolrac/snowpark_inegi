use role accountadmin;

--objetos Snowflake
create database inegi;

--wharehouse
create warehouse inegi_wh 
warehouse_type = 'STANDARD' 
warehouse_size =XSMALL 
auto_suspend = 120 auto_resume = TRUE 
max_cluster_count=1 min_cluster_count=1;

--roles
create role if not exists inegi_role;
grant role inegi_role to user demo;
grant role sysadmin to role inegi_role;

--privilegios  
grant usage on database inegi to role inegi_role;
grant all privileges on schema public to role inegi_role;
grant usage on warehouse inegi_wh to role inegi_role;
