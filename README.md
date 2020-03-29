
Covid-19 Social Conversation and Press Tracking
===========

CovidSocial provides social conversation and press tracking regarding Covid-19/coronavirus. This is a PR emergency project at DKC Analytics. You might find it most useful for tasks involving generating and distributing reports about Covid-19 by running main.py.

Typical usage often looks like this:

    from covidsocial.conversation import Infegy
    from covidsocial.press import Newswhip_article, Newswhip_stats
    
    #type your API keys
    conversation_key = 'conversation_key'
    press_key = 'press_key'


The data source is from two platforms, [Infegy](https://infegy.com/) and [NewsWhip](https://www.newswhip.com/).

You can consult the sample report for the output.
