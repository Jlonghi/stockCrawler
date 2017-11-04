import sys
import os
import subprocess
#Script to create a scrapy spider class and then run the scrapy crawler on google finance
#arg1 is the exchange
#arg2 is the ticker symbol
if(not len(sys.argv) < 3):
    #build the scrapy spider class if it does not exist
    fileName = str(sys.argv[1]) + '_' + str(sys.argv[2]) + '.py'
    if(not os.path.isfile('stockQuotes/spiders/'+fileName)):
        f = open('stockQuotes/spiders/'+fileName, 'w')
        f.write('import scrapy\nclass QuotesSpider(scrapy.Spider):\n\tname="'
        +str(sys.argv[1]) + '_' + str(sys.argv[2])+'"\n\tstart_urls=[\n\t\t\'http://www.google.ca/finance?q='
        +str(sys.argv[1]+'%3A'+sys.argv[2])+'\',\n\t]\n\t'
        +'def parse(self, response):\n\t\tyield{\n\t\t\t\'price\': response.css("span.pr span::text").extract(),\n\t\t\t'
        +'\'change\': response.css("div.id-price-change span span::text").extract(),\n\t\t\t'
        +'\'key\': response.css("td.key::text").extract(),\n\t\t\t'
        +'\'val\':  response.css("td.val::text").extract(),\n\t\t}\n'
        )
        f.close()
    #execute scrapy crawl command on the spider class and create json result
    os.chdir('./stockQuotes')
    #scrapy crawl does not overwrite existing files and gives invalid json if file exists
    #must delete previous files before continuing
    if(os.path.isfile(str('jsonQuotes/'+sys.argv[1]+'_'+sys.argv[2]+'.json'))):
        os.remove(str('jsonQuotes/'+sys.argv[1]+'_'+sys.argv[2]+'.json'))
    print subprocess.check_output(['scrapy','crawl', str(sys.argv[1]+'_'+sys.argv[2]), '-o',str('jsonQuotes/'+sys.argv[1]+'_'+sys.argv[2]+'.json')])
else:
    #change to throw an exception in the future
    print('invalid number of arguments')

