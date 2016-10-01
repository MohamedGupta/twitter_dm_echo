import twitter, twitter_config 
from os import path 
user = 'TheGeoff6Blues' 
states_file = '/users/pi/git/dm_echo/states.dict' 

if path.isfile(states_file):
    states = dict(open(states_file, 'r').read()) 
else:
    states = {'since_id': 0, 'blacklist_users': [], 'blacklist_patterns': []} 

def check_tweets(tw):
    try:
        dms = tw.GetDirectMessages(since_id=states['since_id'])
    except:
        print 'Failed to get dms for ' + user
        return
    if dms:
        states['since_id'] = dms[0].id
        for dm in dms:
            if dm.entities.media.media_url:
                print dm.entities.media.media_url
            tw.PostUpdate(dm.AsDict('text')) 


if __name__ == '__main__':
    cred = twitter_config.accounts[user]
    try:
        tw = twitter.Api(consumer_key=cred['consumer_key'],
                         consumer_secret=cred['consumer_secret'],
                         access_token_key=cred['access_token_key'],
                         access_token_secret=cred['access_token_secret'])
    except Exception, e:
        print e
        print 'Error on init'
        exit()
    check_tweets(tw)
