# ObsidianFileRetrieverSvc
Make sure to setup a cron task to update your local repo 

Add the following line to your cron file  using `crontab -e`
0 * * * * cd /path/to/your/vault && git pull > /dev/null 2>&1

then do `crontab -l` to verify
