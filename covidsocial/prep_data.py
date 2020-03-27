## Before running the pptx, prepare for getting the data or image

from covidsocial.conversation import Infegy
from covidsocial.press import Newswhip_article
import pandas as pd


if __name__ == '__main__':
    infegy = Infegy(api_key= conversation_key)
    state_df = infegy.state()
    dma_df = infegy.dma()
    e_worldcloud = infegy.entity_wordcoud()

    with pd.ExcelWriter('state_dma.xlsx') as writer:
        state_df.to_excel(writer, sheet_name = 'state', index=False)
        dma_df.to_excel(writer, sheet_name =  'dma',index=False)

    news_articles = Newswhip_article(api_key = press_key)
    bigram_fig = news_articles.bigram()

