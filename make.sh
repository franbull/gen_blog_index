#!/usr/bin/env bash
. ~/.bash_profile
workon twittering
. ~/twitter_secrets.sh
cd ~/gen_blog_index
cp ~/instagram_access_token.py .
python gen_blog_index.py
rm instagram_access_token.py
cd ~/francisbullinfo
jekyll build
rsync -r /home/fran/francisbullinfo/_site/* webfaction:/home/fran1/webapps/francisbullinfo/
