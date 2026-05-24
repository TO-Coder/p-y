import requests
import json

url = "https://pbaccess.video.qq.com/trpc.multi_vector_layout.mvl_controller.MVLPageHTTPService/getMVLPage?&vplatform=2"
# url = "https://pbaccess.video.qq.com/trpc.multi_vector_layout.mvl_controller.MVLPageHTTPService/getMVLPage?&vplatform=2"

fromData = {"page_params": {"channel_id": "100173", "filter_params": "sort=75", "page_id": "channel_list",
                            "page_type": "operation"}}

# 因为fromData在浏览器上的格式是json格式，但是你粘贴到pycharm中之后就变成python的数据类型 字典，这里要将字典转为json
fromData = json.dumps(fromData)

# 1.user-agent 2.cookie 3.content-type 4.origin 5.referer
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
    "cookie": "qq_domain_video_guid_verify=49d939c863327ea3; _qimei_uuid42=18a1e170a111000b55ae2ef132ccfe0e3080b286e2; video_platform=2; video_guid=49d939c863327ea3; _qimei_h38=19c5a01055ae2ef132ccfe0e02000005318a1e; pgv_pvid=9648729840; _qimei_q32=f30a0665f1f63233a341ca4a0b25f731; _qimei_q36=65000dad1bc3081a2396f53e300017418901; RK=CCdpVnp3kQ; ptcz=d47ae5e603d446c8da4baa785639c9dc27839ac622022b4281b20191901ab15a; check_16=3a3e157bef091ccbce7c107d0cffc796; eas_sid=q1X7r3f6C0o0w3a5K5x1Y0u6k6; _qimei_fingerprint=5407e2bd0b13ec0d2a8ba9e55df03a5d; yyb_muid=3262841CD92C6965068A9139D80968E1; pac_uid=0_QmrA6Zi4K28ry; pgv_info=ssid=s8649008736; _qimei_i_3=40e27f8ac75d54d8c5c3fa665c8c22b4f3ebaca31b5c0a8ae28a200a2ec0253f686b34943c89e2bcb7b3; video_omgid=49d939c863327ea3",
    "content-type": "application/json",
    "origin": "https://v.qq.com",
    "referer": "https://v.qq.com/",
}

resp = requests.post(url, headers=header, data=fromData)

data = resp.json()

# print(data)

for i in data['data']['modules']['normal']['cards'][0]['children_list']['poster_card']['cards']:
    movie_name = i['params']['title']
    score_josn = i['params']['latest_mark_label']
    score_dict = json.loads(score_josn)  # 将json格式的字符串转换为字典
    score_dict = score_dict['4']["info"]['text']
    movie_img = i['params']['new_pic_vt']
    print(movie_name)
    print(score_dict)
    print(movie_img)


resp.close()
