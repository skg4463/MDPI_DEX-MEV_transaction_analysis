## Decentralized exchange transaction analysis and MEV attack identification: Focusing on Uniswap USDC3
Nakhoon Choi, Heeyoul Kim 


![Data collection and analysis process for DEX analysis.](https://github.com/skg4463/MDPI_DEX-MEV_transaction_analysis/assets/45844164/43da90b2-011e-4b10-bba9-e10236a608fc)
ㄴFigure. Data collection and analysis process for DEX analysis.

**Please prepare your own API KEY for use.**

### Classification:
	data-*   : Data used for analysis
	dataEX-* : Extraction means to obtain data
	grpdrw-* : Drawing graphs through data


### dataEX method:
	Etherscan.io Transaction Extractor
 	Etherscan API
	Transpose.io SDK
            
### Discription
#### Data Extractor
- **dataEX-EtherAPI_get_token_transfer.py**
  - Ethersca API, 
  - -> data-(from-etherscanAPI)_uniswap_transactions*.csv
  - 'blockNumber', 'timeStamp', 'transactionHash', 'sender', 'to', 'data', 'gasPrice', 'gasUsed'
    - data:  
        - amount0     
        - amount1	    
        - sqrtPriceX96
        - liquidity   
        - tick        


- **dataEX-EtherAPI_get_token_transfer_gasPriceOnly.py**
  - Ethersca API, 
  - -> data-aggregated_gas_prices*.csv


- **dataEX-sdk_base_endpoint_swaps.py**
  - Transpose API-base endpoint,


- **dataEX-sdk_custom_endpoint_liqui.py**
  - Transpose API-custom endpoint, https://api.transpose.io/endpoint/dex_liquidity_by_account?end_date={end_date}&start_date={start_date}
  - -> data-(from-trans)_uniswap_data_*.csv





