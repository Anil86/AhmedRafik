from datetime import datetime

from scrapy import Spider
from scrapy.http.request.json_request import JsonRequest
from scrapy.http.response.text import TextResponse

from AhmedRafik.Helpers.UrlHelpers import UrlHelpers


# ToDo: Airbnb: Decode url
# ToDo: Airbnb: Send request headers
# ToDo: Airbnb: Add cookie
# ToDo: Airbnb: Update time in cookie
# ToDo: Airbnb: Listing details
# ToDo: Airbnb: Listing reviews

class AirbnbSpider(Spider):
    name = 'Airbnb'
    allowed_domains = ['airbnb.co.in']

    _headers = \
        {
            'Authority': 'www.airbnb.co.in',
            'Accept': '*/*',
            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
            'Content-Type': 'application/json',
            'device-memory': '8',
            'Dpr': '1.25',
            'Ect': '4g',
            'Referer': 'https://www.airbnb.co.in/?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&search_mode=flex_destinations_search&flexible_trip_lengths%5B%5D=one_week&location_search=MIN_MAP_BOUNDS&category_tag=Tag%3A4104&search_type=category_change',
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'viewport-width': '1286',
            'x-airbnb-api-key': 'd306zoyjsyarp7ifhu67rjxn52tv0t20',
            'x-airbnb-graphql-platform': 'web',
            'x-airbnb-graphql-platform-client': 'minimalist-niobe',
            'x-airbnb-supports-airlock-v2': 'true',
            'x-client-request-id': '0a43kpg1li2k3w0xgfp5n0lvntp9',
            'x-csrf-token': 'null',
            'x-csrf-without-token': '1',
            'x-niobe-short-circuited': 'true'
        }

    def start_requests(self):
        url = "https://www.airbnb.co.in/api/v3/ExploreSections?operationName=ExploreSections&locale=en-IN&currency=INR&variables=%7B%22isInitialLoad%22%3Atrue%2C%22hasLoggedIn%22%3Afalse%2C%22cdnCacheSafe%22%3Afalse%2C%22source%22%3A%22EXPLORE%22%2C%22exploreRequest%22%3A%7B%22metadataOnly%22%3Afalse%2C%22version%22%3A%221.8.3%22%2C%22itemsPerGrid%22%3A20%2C%22tabId%22%3A%22home_tab%22%2C%22refinementPaths%22%3A%5B%22%2Fhomes%22%5D%2C%22searchMode%22%3A%22flex_destinations_search%22%2C%22flexibleTripLengths%22%3A%5B%22one_week%22%5D%2C%22locationSearch%22%3A%22MIN_MAP_BOUNDS%22%2C%22searchType%22%3A%22category_change%22%2C%22categoryTag%22%3A%22Tag%3A4104%22%2C%22cdnCacheSafe%22%3Afalse%2C%22treatmentFlags%22%3A%5B%22flex_destinations_june_2021_launch_web_treatment%22%2C%22merch_header_breakpoint_expansion_web%22%2C%22flexible_dates_12_month_lead_time%22%2C%22storefronts_nov23_2021_homepage_web_treatment%22%2C%22lazy_load_flex_search_map_compact%22%2C%22lazy_load_flex_search_map_wide%22%2C%22im_flexible_may_2022_treatment%22%2C%22im_flexible_may_2022_treatment%22%2C%22flex_v2_review_counts_treatment%22%2C%22flexible_dates_options_extend_one_three_seven_days%22%2C%22super_date_flexibility%22%2C%22micro_flex_improvements%22%2C%22micro_flex_show_by_default%22%2C%22search_input_placeholder_phrases%22%2C%22pets_fee_treatment%22%5D%2C%22screenSize%22%3A%22large%22%2C%22isInitialLoad%22%3Atrue%2C%22hasLoggedIn%22%3Afalse%2C%22itemsOffset%22%3A0%2C%22sectionOffset%22%3A0%2C%22federatedSearchSessionId%22%3A%22bea038cc-6d0d-4c6f-8850-54175804df20%22%7D%2C%22gpRequest%22%3A%7B%22expectedResponseType%22%3A%22INCREMENTAL%22%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%222cdce1506215cc50757034614e5780de66a5d17b0c204f75d3ae1a45ceae21e4%22%7D%7D"

        cookiesText = 'bev=1659213414_MGYxOWE1MWMzNGU0; tzo=330; cdn_exp_b910f64ca3b409af4=treatment; cdn_exp_edca6a5ab9666c814=treatment; cdn_exp_7b27e8582f6ea5b25=control; cdn_exp_fea7ec9bd22598e31=control; cdn_exp_664025b35de9ca5f8=treatment; cdn_exp_29e65ed560e5fd9f1=control; cdn_exp_d92fdc77c0b0762c0=control; cdn_exp_255f380963191f229=treatment; OptanonAlertBoxClosed=NR; frmfctr=wide; _user_attributes=%7B%22guest_exchange%22%3A79.217%2C%22device_profiling_session_id%22%3A%221659213772--ff89679e4417d38b476cf496%22%2C%22giftcard_profiling_session_id%22%3A%221659440578--25c694904a73214f83a4b589%22%2C%22reservation_profiling_session_id%22%3A%221659440578--7b1a68eba5ca3d98ac132739%22%2C%22curr%22%3A%22INR%22%7D; _abck=F612608668BDF9D61DA964FC86FD96E5~0~YAAQr/hWuNugxjuCAQAAdL9dXgjcK0VVu5s+x5mSwZgNcgPPX8TCbNqJLI2WkMUniMw6jiaK+hxEAMPJa1325d2rtmN7qydARz+RO340VD0Ofqa5Z/mipaS4AffR+tgEfUlqeNM/K2DixoQ0WCWHk5X8adOy8JSPCUAmzFqJS1gN0T1jmLJIWxxVU1frwPX7R/bIH2d3TMtp3pReik8+OnJcJLmujw6iTmRjNfnJ37fppbsbaXPj80EZv0Txmw3Tj0N+F6UVnkYAsgV43X6FI+bvrh7hVyoqz7NPsWNuhYt2hXGQBp1LwqoDiSxTcE0vR+z9lz9mgTQQeGOrRiiBX6oMkhNOJm5A6yiQcwj23jf2iUsdMY6HGOHYumqDox2qmCsOM+oA+ML1+27CpkhUawE8xUW80hNPxYB9~-1~-1~-1; bm_sz=CC82E8F274DCB07FFA668D078564D115~YAAQr/hWuNygxjuCAQAAdL9dXhCoEbiO58EfyZi1mIyBMZt2lNxyxlbAmP59la1ZZEhncyS4MRhFHJfqY4AwyenoFaicyJ/AVd5b6WJKuWsbYSjUi2iTZlZriqnbyUUxDAzvBSGWT2yxOGv0H4OfDSbwY6kAfnqjOKLntWXjFPL8Fcqq2RMA9zyFLSwE5oQP3begrCWSEwvo5LVJSvd44wr6svGp6cMDvBzp/eWqEU0VNIPcBoMWFn1tponIuf5591cQgNoV0ap6HDWt3qQ7GXY3E3jGhXfE3GFmX5+i/7wIxcpOCg==~3687494~4469048; jitney_client_session_created_at=1659440580; jitney_client_session_id=95622c90-d8e4-4766-8d13-b0fe4c4be888; previousTab=%7B%22id%22%3A%22c9cdedc9-9ebf-4162-86f3-824fecaae1ef%22%2C%22url%22%3A%22https%3A%2F%2Fwww.airbnb.co.in%2F%22%7D; jitney_client_session_updated_at=1659440624; cfrmfctr=DESKTOP; cbkp=3'
        cookies = UrlHelpers.ParseCookie(cookiesText)
        epoch = round(datetime.now().timestamp())
        cookies["jitney_client_session_created_at"] = epoch
        cookies["jitney_client_session_updated_at"] = epoch

        yield JsonRequest(url=url, headers=self._headers, cookies=cookies, errback=self.ErrorHandler)

    def parse(self, response: TextResponse):
        self.logger.info(f"{response.text}")

    def ErrorHandler(self, failure):
        self.logger.error(str(failure))