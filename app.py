"""동대문 여성복 답사 노트 — Streamlit 공개 페이지.

내용은 2026-11-17에 공개 블로그·기사에서 모은 것이다. 출처 탭에 링크와 작성 시점을 적었다.
"""
from urllib.parse import quote

import streamlit as st

st.set_page_config(page_title="동대문 여성복 답사 노트", page_icon="🧵", layout="centered")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap');
:root{
  --ink:#1d2140; --muted:#5d6280; --line:#dcdeea; --surface:#ffffff;
  --indigo:#2f3a8f; --rose:#c2185b; --rose-soft:#fbe4ee; --indigo-soft:#e5e8fa;
  --ok:#2e7d4f; --warn:#a15c00; --bad:#b3261e; --warn-soft:#fff1dc; --bad-soft:#fde7e5;
  --night:#272d63; --day:#e8b64c;
}
html, body, [class*="st-"], .stMarkdown, .stTabs { font-family:"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif; }
.g h1,.g h2,.g h3{font-family:"Do Hyeon","IBM Plex Sans KR",sans-serif;font-weight:400;margin:0;line-height:1.25;color:var(--ink)}
.g h1{font-size:clamp(28px,6vw,40px)}
.g h2{font-size:24px;color:var(--indigo);margin:8px 0 6px}
.g h3{font-size:18px}
.g p{margin:0;color:var(--ink);line-height:1.7}
.g .sub{color:var(--muted);font-size:14.5px;line-height:1.7}
.g .note{color:var(--muted);font-size:13px;line-height:1.6;margin-top:6px}
.g .eyebrow{font-size:12px;letter-spacing:.12em;color:var(--rose);font-weight:700}
.g .stack{display:flex;flex-direction:column;gap:12px}
.g .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin:8px 0}
.g .card{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px 16px;display:flex;flex-direction:column;gap:8px;min-width:0}
.g .card.feature{border:2px solid var(--rose)}
.g .card.dead{background:var(--bad-soft);border-color:var(--bad)}
.g .card ul{margin:0;padding-left:18px;font-size:14px;color:var(--muted);display:flex;flex-direction:column;gap:3px;line-height:1.6}
.g .top{display:flex;justify-content:space-between;align-items:flex-start;gap:8px;flex-wrap:wrap}
.g .chip{display:inline-flex;align-items:center;font-size:12px;padding:2px 9px;border-radius:999px;border:1px solid var(--line);background:var(--surface);color:var(--muted);white-space:nowrap}
.g .chip.ok{color:var(--ok);border-color:var(--ok)}
.g .chip.warn{color:var(--warn);border-color:var(--warn);background:var(--warn-soft)}
.g .chip.bad{color:var(--bad);border-color:var(--bad);background:var(--bad-soft)}
.g .chip.rose{color:var(--rose);border-color:var(--rose);background:var(--rose-soft)}
.g .tags{display:flex;flex-wrap:wrap;gap:6px}
.g .tbl{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--surface);margin:8px 0}
.g table{border-collapse:collapse;width:100%;min-width:520px;font-size:14px}
.g th,.g td{text-align:left;padding:9px 11px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink)}
.g th{font-size:12.5px;color:var(--muted);font-weight:500}
.g tr:last-child td{border-bottom:0}
.g .slip{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:14px 16px 12px;display:flex;flex-direction:column;gap:8px;min-width:0}
.g .slip-head{display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:wrap}
.g .hours{font-variant-numeric:tabular-nums;font-size:13px;color:var(--indigo);font-weight:700}
.g .slip p{font-size:14px;color:var(--muted)}
.g .maps{display:flex;gap:10px;font-size:13.5px;flex-wrap:wrap}
.g a{color:var(--indigo);text-underline-offset:3px}
.g .steps{display:flex;flex-direction:column;gap:10px;counter-reset:s;margin:8px 0}
.g .step{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px 16px;counter-increment:s}
.g .step b::before{content:counter(s) ". ";color:var(--rose)}
.g .step p{font-size:14px;color:var(--muted);margin-top:4px}
.g .callout{background:var(--warn-soft);border:1px solid var(--warn);border-radius:10px;padding:12px 16px;font-size:14px;color:var(--ink);line-height:1.6}
.g .tl{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px;overflow-x:auto}
.g .tl-inner{min-width:480px;display:grid;grid-template-columns:105px 1fr;row-gap:8px;column-gap:12px;align-items:center}
.g .tl-name{font-size:13.5px;font-weight:500;color:var(--ink);white-space:nowrap}
.g .tl-name small{display:block;color:var(--muted);font-weight:400;font-size:11.5px}
.g .tl-track{position:relative;height:22px;border-radius:4px;background:repeating-linear-gradient(90deg,var(--line) 0 1px,transparent 1px calc(100%/8))}
.g .tl-bar{position:absolute;top:3px;bottom:3px;border-radius:4px;background:var(--night)}
.g .tl-bar.day{background:var(--day)}
.g .tl-bar.best{box-shadow:inset 0 0 0 2px var(--rose)}
.g .tl-shade{position:absolute;top:0;bottom:0;background:var(--indigo-soft);opacity:.6;border-radius:4px}
.g .tl-axis{position:relative;height:18px;font-size:11px;color:var(--muted)}
.g .tl-axis span{position:absolute;transform:translateX(-50%)}
.g .legend{display:flex;flex-wrap:wrap;gap:14px;font-size:12.5px;color:var(--muted);margin-top:10px}
.g .sw{display:inline-block;width:14px;height:10px;border-radius:2px;vertical-align:middle;margin-right:5px}
</style>
"""
st.html(CSS)


def block(html: str) -> None:
    st.html(f'<div class="g">{html}</div>')


def map_links(query: str) -> str:
    q = quote(query)
    return (f'<div class="maps"><a href="https://map.naver.com/p/search/{q}" target="_blank">네이버 지도</a>'
            f'<a href="https://map.kakao.com/?q={q}" target="_blank">카카오맵</a></div>')


# ---------------------------------------------------------------- 머리말
block("""
<div class="stack">
  <div class="eyebrow">2026-11-17 정리 · 여성의류 쇼핑몰 창업 준비</div>
  <h1>동대문 여성복 답사 노트</h1>
  <p class="sub">사업자등록 전에 밤 10시쯤 동대문 도매상가를 먼저 둘러보려는 사람을 위한 정리입니다.
  내일 답사 계획, 매장 위치, 영업시간, 쇼핑몰 창업 절차, 도매 앱·사이트를 탭으로 나눴습니다.
  공개된 블로그·기사만 읽어서 모았고, 영업시간과 조건은 자주 바뀌니 가기 전에 한 번 더 확인하세요.</p>
</div>
""")

tab_trip, tab_shops, tab_hours, tab_start, tab_apps, tab_src = st.tabs(
    ["내일 답사", "매장·위치", "영업시간", "쇼핑몰 창업 절차", "도매 앱·사이트", "출처"]
)

# ---------------------------------------------------------------- 내일 답사
with tab_trip:
    block("""
<h2>사업자 없이 가도 되나</h2>
<div class="cards">
  <div class="card feature">
    <div class="top"><h3>둘러보는 건 됩니다</h3><span class="chip ok">답사 OK</span></div>
    <ul>
      <li>사업자등록증 없이도 상가에 들어가 구경할 수 있습니다. 다만 도매가 구매는 제한될 수 있습니다.</li>
      <li>사입 셀러들도 처음엔 많이 사지 말고 분위기부터 익히라고 권합니다. 어떤 스타일이 많이 걸렸는지, 어느 매장에 손님이 몰리는지만 봐도 유행이 보입니다.</li>
      <li>하루로는 감이 잘 안 와서 여러 번 가 보라는 조언도 있습니다.</li>
    </ul>
  </div>
  <div class="card">
    <div class="top"><h3>사는 건 조심</h3><span class="chip warn">구매 제한</span></div>
    <ul>
      <li>도매 매장은 보통 2장 이상 팔고 낱장은 잘 안 팝니다. 처음 온 사람에게 사업자등록증을 묻는 곳도 있습니다.</li>
      <li>첫날은 "보는 날"로 정하는 게 편합니다. 물어보면 "창업 준비 중이라 둘러보는 중"이라고 솔직하게.</li>
    </ul>
  </div>
</div>

<h2>밤 답사 동선 (22시 출발 기준)</h2>
<p class="sub">처음 가는 사람에게 추천되는 시간은 밤 10~11시입니다. 8시 오픈 직후는 진열·주문 처리로 바쁘고, 22시쯤부터 여유가 생겨 물어보기 좋습니다. 2~3시간 잡으세요.</p>
<div class="tbl"><table>
<thead><tr><th>시간</th><th>할 일</th><th>메모</th></tr></thead>
<tbody>
<tr><td>출발 전</td><td>볼 품목 2~3개만 정하기 (예: 니트·원피스·슬랙스)</td><td>계획 없이 가면 예쁜 것만 보다 끝남</td></tr>
<tr><td>21:30</td><td>동대문역사문화공원역 도착, 화장실·편의점</td><td>운동화, 가벼운 가방, 보조배터리</td></tr>
<tr><td>22:00–23:00</td><td>APM PLACE → 뉴존 → 디자이너클럽</td><td>모두 20시에 여는 밤 상가</td></tr>
<tr><td>23:00–24:00</td><td>더블유(W) 등 작은 상가, 또는 메모 정리</td><td>디오트는 자정, 청평화는 23시에 열기 시작</td></tr>
<tr><td>00:00–01:30</td><td>질문은 피하고 눈으로만</td><td>카톡·앱 주문 출고가 몰리는 시간</td></tr>
<tr><td>01:00 이후</td><td>체력이 되면 디오트·청평화</td><td>여성복 거래처가 가장 많이 모인 곳. 지하철 끊기니 귀갓길 확인</td></tr>
</tbody></table></div>
<p class="note">지하철로 돌아오려면 자정 전에 끝내야 하니 APM PLACE·뉴존·디자이너클럽만 보는 게 현실적입니다. 막차 시간은 지도 앱에서 확인하세요.</p>

<h2>현장에서 쓰는 말</h2>
<div class="tbl"><table>
<thead><tr><th>동대문 말</th><th>뜻</th><th>예</th></tr></thead>
<tbody>
<tr><td>언니·이모 / 삼촌</td><td>여자 사장님 / 남자 사장님</td><td></td></tr>
<tr><td>상호</td><td>쇼핑몰 이름</td><td>"어디서 오셨어요?" = 상호가 뭐냐는 뜻</td></tr>
<tr><td>어떻게 나왔어요?</td><td>가격이 얼마예요?</td><td>"8,000원이요"</td></tr>
<tr><td>단가 / 깔</td><td>도매가 / 색상</td><td>"이거 깔 몇 개 나와요?"</td></tr>
<tr><td>낱장</td><td>한 장</td><td>도매는 낱장 판매를 꺼리는 곳이 많음</td></tr>
<tr><td>장끼</td><td>영수증(거래 명세)</td><td></td></tr>
<tr><td>미송</td><td>재고 없을 때 돈 먼저 내고 입고되면 받기</td><td>"월밤" = 월요일 밤 입고</td></tr>
<tr><td>리오더</td><td>재주문</td><td></td></tr>
</tbody></table></div>

<h2>하면 좋은 것 · 하지 말 것</h2>
<div class="cards">
  <div class="card"><h3>하면 좋은 것</h3><ul>
    <li>상가·층·호수, 품목, 단가, 색상 수를 휴대폰 메모에 바로 적기 (아래 양식)</li>
    <li>마음에 드는 매장의 상호·호수 기억하기, 명함 있으면 받기</li>
    <li>손님이 몰린 매장, 통로에 많이 걸린 스타일 보기</li>
    <li>같은 품목도 층마다 단가가 다름 (디오트는 1~2층과 3~4층의 단가·스타일이 다르다는 글)</li>
    <li>밤이니 같이 다니고 귀중품 조심</li>
  </ul></div>
  <div class="card"><h3>하지 말 것</h3><ul>
    <li>허락 없이 상품 사진 찍기 (매장마다 촬영 제한이 있음)</li>
    <li>바쁜 매장 오래 붙잡기, 과한 흥정</li>
    <li>마음에 든다고 그 자리에서 많이 사기</li>
    <li>걸린 옷 마구 꺼내 보기. 보고 싶으면 먼저 물어보기</li>
  </ul></div>
  <div class="card"><h3>돈 감 잡기</h3><ul>
    <li>보기만 할 거면 현금은 조금만</li>
    <li>셀러 가이드 기준 첫 사입은 10상품 × 2색, 25~30만 원 정도 (여름 기준)</li>
    <li>초여름 단가 감: 티셔츠 1만 원 이하, 원피스 2만 원 이하, 아우터 3만 원 이하</li>
  </ul></div>
  <div class="card"><h3>차로 간다면</h3><ul>
    <li>상가 주차장보다 DDP 지하주차장이나 근처 주차장이 더 싸다는 팁</li>
    <li>오픈 30분쯤 지나야 상가가 살아남</li>
  </ul></div>
</div>

<h2>답사 기록 양식</h2>
<div class="tbl"><table>
<thead><tr><th>상가·층·호수</th><th>상호</th><th>품목</th><th>단가</th><th>색상 수</th><th>사이즈</th><th>소재·느낌</th><th>메모</th></tr></thead>
<tbody><tr><td>예: 뉴존 2층</td><td>(간판 이름)</td><td>니트 가디건</td><td>(들은 가격)</td><td>4</td><td>프리</td><td>도톰, 보풀 적음</td><td>손님 많음</td></tr></tbody>
</table></div>

<h2>낮에 가 볼 곳: DDP 쇼룸</h2>
<div class="card feature">
  <div class="top"><h3>DDP 쇼룸 2층 샘플스토어</h3><span class="chip ok">무료 · 사업자 없이 가능</span></div>
  <ul>
    <li>서울시·서울경제진흥원이 DDP 디자인랩 1~2층에 연 쇼룸. 동대문 상품을 직접 입어 보고 사진도 찍을 수 있음</li>
    <li>이용 후기 기준 개인·학생도 사전 예약하면 무료, 실물 신분증 필요</li>
    <li>10:00–19:00, 주말·공휴일엔 샘플·장비 대여 불가. 한 번에 최대 5항목</li>
    <li>스튜디오는 예약이 꽉 차는 편이라 미리 잡기</li>
  </ul>
  """ + map_links("DDP 디자인랩") + """
</div>
""")

# ---------------------------------------------------------------- 매장·위치
SHOPS = [
    dict(n="APM PLACE", s=20, e=5, women=True, best=True, q="동대문 APM PLACE",
         note="매장이 넓고 통로가 여유로움. 여성복이면 특히 추천.", tags=["여성복", "22시 이후 추천"]),
    dict(n="뉴존(누죤)", s=20, e=5, women=True, best=True, q="동대문 누죤",
         note="인기·신상 상품을 통로 쪽에 진열하고 오픈형 매장이 많아 보기 편함.", tags=["여성복", "남성복", "22시 이후 추천"]),
    dict(n="디자이너클럽", s=20, e=5, women=True, best=True, q="동대문 디자이너클럽",
         note="여성복 전문. 가방·액세서리 등 잡화 품질이 좋은 거래처가 많다는 평.", tags=["여성복", "잡화", "22시 이후 추천"]),
    dict(n="더블유(W)", s=None, e=None, women=True, best=True, q="동대문 스튜디오W",
         note="빅사이즈 여성복 거래처가 있음. 규모가 작아 금방 둘러봄. 영업시간은 자료에 없음. 지도에서 '스튜디오W'로 찾아보고 맞는지 확인.",
         tags=["여성복", "빅사이즈"]),
    dict(n="디오트", s=24, e=12, women=True, best=True, q="동대문 디오트",
         note="여성복 거래처가 가장 많이 모인 대표 상가. 서울 중구 다산로 293. 동대문역 8번 출구 또는 동대문역사문화공원역 14·2번 출구(블로그 안내).",
         tags=["여성복", "01시 이후 추천"]),
    dict(n="청평화", s=23, e=12, women=True, best=True, q="청평화시장",
         note="디오트 맞은편(오래된 자료 기준). 30대 이상 여성복이 많고 재고 상품 위주라 반품이 어렵다는 글.",
         tags=["여성복", "01시 이후 추천", "반품 주의"]),
    dict(n="APM", s=20, e=5, women=False, best=False, q="동대문 APM",
         note="매장 정리가 깔끔하고 거래처 개성이 뚜렷해 처음 가도 비교하기 좋음.", tags=["남녀"]),
    dict(n="벨포스트", s=20, e=5, women=False, best=False, q="동대문 벨포스트",
         note="국내 생산 비중이 높아 품질은 좋지만 단가가 조금 높음.", tags=["국내 생산", "품질"]),
    dict(n="신평화", s=21, e=17, women=False, best=False, q="신평화시장",
         note="B1·1·4층은 다음 날 17시, 2·3층은 10시까지. 숙녀복·란제리 매장이 많다는 오래된 글.", tags=["숙녀복"]),
    dict(n="남평화", s=24, e=12, women=False, best=False, q="남평화시장",
         note="가방 도매로 알려진 상가(오래된 글 기준).", tags=["가방"]),
    dict(n="서평화", s=9, e=21, women=False, best=False, q="서평화시장",
         note="낮에 여는 상가.", tags=["낮 시장"]),
]


def fmt(h):
    return f"{h % 24:02d}:00"


with tab_shops:
    block("""
<h2>여성복 추천 매장과 위치</h2>
<p class="sub">여성복 추천 동선: APM PLACE → 뉴존 → 디오트 → 디자이너클럽 → 더블유(W) → 청평화 (사입 블로그 montips, 2026-07).
모두 동대문역사문화공원역·동대문역 근처에 모여 있습니다. 정확한 위치는 각 카드의 지도 링크로 확인하세요.</p>
""")
    only_women = st.toggle("여성복 추천 상가만 보기", value=True, key="only_women")
    shown = [s for s in SHOPS if s["women"] or not only_women]
    cards = []
    for s in shown:
        hrs = "시간 미확인" if s["s"] is None else f"{fmt(s['s'])}–{fmt(s['e'])}"
        tags = "".join(
            f'<span class="chip {"rose" if "추천" in t else "warn" if "주의" in t else ""}">{t}</span>' for t in s["tags"]
        )
        cards.append(f'<article class="slip"><div class="slip-head"><h3>{s["n"]}</h3><span class="hours">{hrs}</span></div>'
                     f'<p>{s["note"]}</p><div class="tags">{tags}</div>{map_links(s["q"])}</article>')
    block(f'<div class="cards">{"".join(cards)}</div>')

# ---------------------------------------------------------------- 영업시간
with tab_hours:
    START, SPAN = 18, 24

    def pos(h):
        x = h - START
        return x + 24 if x < 0 else x

    rows = []
    for s in SHOPS:
        if s["s"] is None or s["s"] < 12:  # 낮 상가(서평화)는 축 밖이라 카드에만 둠
            continue
        a = pos(s["s"] % 24)
        z = pos(s["e"])
        if z <= a:
            z += 24
        z = min(z, SPAN)
        day = 6 <= s["s"] < 18
        sa, sz = pos(22), pos(1.5)
        rows.append(
            f'<div class="tl-name">{s["n"]}<small>{fmt(s["s"])}–{fmt(s["e"])}</small></div>'
            f'<div class="tl-track"><div class="tl-shade" style="left:{sa/SPAN*100:.2f}%;width:{(sz-sa)/SPAN*100:.2f}%"></div>'
            f'<div class="tl-bar {"day" if day else ""} {"best" if s["best"] else ""}" style="left:{a/SPAN*100:.2f}%;width:{(z-a)/SPAN*100:.2f}%"></div></div>'
        )
    axis = "".join(f'<span style="left:{i/SPAN*100:.2f}%">{(START+i)%24:02d}시</span>' for i in range(0, SPAN + 1, 3))
    block(f"""
<h2>상가는 언제 열리나</h2>
<p class="sub">2026년 7월 사입 블로그(montips) 기준. 가로축은 저녁 6시부터 다음 날 저녁 6시까지입니다.
분홍 테두리는 여성복 추천 상가. 명절·여름휴가·행사 때는 바뀝니다. 서평화(09–21시)와 DDP 쇼룸(평일 10–19시)은 낮에 엽니다.</p>
<div class="tl"><div class="tl-inner"><div></div><div class="tl-axis">{axis}</div>{"".join(rows)}</div>
<div class="legend"><span><i class="sw" style="background:var(--night)"></i>밤 영업</span>
<span><i class="sw" style="background:var(--day)"></i>낮 영업</span>
<span><i class="sw" style="background:var(--indigo-soft)"></i>22:00–01:30 (22–23시 추천, 자정~01:30 출고로 바쁨)</span></div></div>
<p class="note">피하면 좋은 시간: 20시 직후(진열 중), 자정~01:30(주문 출고), 02~03시(직원 식사 시간).</p>
""")

# ---------------------------------------------------------------- 창업 절차
with tab_start:
    block("""
<h2>개인 쇼핑몰 차리는 순서</h2>
<div class="steps">
  <div class="step"><b>답사·상품 방향 정하기</b><p>누구에게 어떤 옷을 팔지(연령대, 스타일, 가격대)부터 정합니다. 답사 기록과 DDP 쇼룸 착용 사진으로 감을 잡습니다.</p></div>
  <div class="step"><b>사업자등록 (국세청 홈택스)</b><p>온라인으로 신청할 수 있고, 업종은 전자상거래 소매업으로 고릅니다. 사업을 시작한 날부터 20일 안에 신청하라고 안내됩니다. 매출이 작으면 간이과세자로 시작할 수 있습니다(기준은 홈택스에서 확인).</p></div>
  <div class="step"><b>통신판매업 신고 (정부24)</b><p>사업자등록증, 대표자 신분증, 그리고 선결제로 파는 경우 구매안전서비스 이용확인증(결제대행사나 판매 플랫폼에서 발급)이 필요합니다. 규모가 작으면 면제되는 경우가 있으니 정부24·구청에서 확인하세요. 처리는 며칠 걸립니다.</p></div>
  <div class="step"><b>판매할 곳 고르기</b><p>네이버 스마트스토어처럼 입점형으로 시작하거나, 카페24·아임웹 같은 자사몰을 열거나, 에이블리·지그재그 같은 여성 패션 앱에 입점합니다. 처음엔 한 곳에서 시작하는 게 관리가 쉽습니다.</p></div>
  <div class="step"><b>도매 거래 시작</b><p>사업자등록증이 생기면 신상마켓 가입, 답사 때 적어 둔 매장에서 샘플 사입(판매할 색 위주, 보통 2장 이상).</p></div>
  <div class="step"><b>촬영·상세페이지</b><p>DDP 쇼룸 스튜디오(무료 예약)나 집에서 착용 사진. 실측 사이즈, 소재, 세탁 방법을 적습니다.</p></div>
  <div class="step"><b>배송·반품 정하기</b><p>택배사 계약, 교환·반품 기준을 미리 적어 둡니다. 도매 매장은 반품이 어려운 곳이 많아 검수(구성품, 케어라벨, 불량)가 중요합니다.</p></div>
  <div class="step"><b>주문이 늘면 대행</b><p>사입삼촌이나 셀업 같은 사입 대행으로 밤마다 직접 가는 일을 줄입니다.</p></div>
</div>
<div class="callout">세금·신고 기준(간이과세 매출 기준, 통신판매업 면제 조건, 등록면허세)은 바뀔 수 있습니다. 신청 전에 홈택스·정부24 공식 안내를 확인하세요.</div>
""")

# ---------------------------------------------------------------- 도매 앱·사이트
with tab_apps:
    block("""
<h2>도매처 정보가 있는 앱·사이트</h2>
<p class="sub">지금 실제로 쓰이는 건 신상마켓이 대표이고, 셀업은 주문·사입삼촌 관리 쪽입니다. 둘 다 사업자 인증이 있어야 상품과 거래처를 볼 수 있습니다.</p>
<div class="cards">
  <div class="card feature">
    <div class="top"><h3>신상마켓</h3><span class="chip ok">운영 · 사업자 인증</span></div>
    <ul>
      <li>동대문 도매매장과 소매 사업자를 잇는 앱. 누적 도매매장 약 1만7천 곳이라고 소개</li>
      <li>상품 보기, 주문, 결제, 세금계산서, 재고 문의(신상톡)</li>
      <li>신상배송: 여러 매장 주문을 사입부터 택배까지 대신</li>
      <li>사업자등록증 승인 필요, 일반 소비자 가입 불가</li>
    </ul>
  </div>
  <div class="card">
    <div class="top"><h3>셀업 (SELL UP)</h3><span class="chip ok">운영</span></div>
    <ul>
      <li>도매·소매·사입삼촌을 잇는 주문·정산 앱</li>
      <li>사입삼촌 매칭·주문 관리를 월 정액으로 제공한다고 소개, 초보 셀러 강의도 엶</li>
    </ul>
  </div>
  <div class="card">
    <div class="top"><h3>도매꾹·도매매</h3><span class="chip ok">종합 도매</span></div>
    <ul>
      <li>의류 전문이 아닌 종합 도매몰. 일반 고객도 일부 구매 가능</li>
      <li>잡화·소품 보충용</li>
    </ul>
  </div>
  <div class="card">
    <div class="top"><h3>원패브릭</h3><span class="chip ok">원·부자재</span></div>
    <ul>
      <li>동대문 원단·부자재 업체 100여 곳 입점 소개. 나중에 직접 만들 때 원단·단추·라벨용</li>
    </ul>
  </div>
  <div class="card dead">
    <div class="top"><h3>링크샵스 · 골라라</h3><span class="chip bad">서비스 종료</span></div>
    <ul>
      <li>링크샵스는 2024년 서비스 종료·폐업. 옛 블로그 글엔 아직 추천으로 나오니 주의</li>
      <li>대행·플랫폼에 선결제를 크게 걸어 두지 않기</li>
    </ul>
  </div>
</div>

<h2>사입삼촌</h2>
<p class="sub">밤에 도매 매장에서 주문한 물건을 찾아 계산하고 보내 주는 사입 대행인입니다. 건당 계약(주문이 적을 때)과 월 계약(주문이 꾸준할 때)이 있고, 공개된 금액은 없어 견적을 받아 비교해야 합니다.
막 시작한 쇼핑몰은 구하기 어려울 수 있어 셀업 같은 매칭 서비스를 씁니다.</p>

<h2>참고할 정보 사이트</h2>
<div class="tbl"><table>
<thead><tr><th>사이트</th><th>쓸모</th></tr></thead>
<tbody>
<tr><td><a href="https://montips.com/dongdaemun-market-hours/" target="_blank">montips</a></td><td>상가별 영업시간, 여성복 동선, 초보 가이드 (2026-07)</td></tr>
<tr><td><a href="https://home.buy-now.kr/blog/articles/2026-dongdaemun-summer" target="_blank">바이나우 블로그</a></td><td>상가별 휴가·명절 휴무 일정</td></tr>
<tr><td><a href="https://square.a-bly.com/tipsbeginner-3" target="_blank">에이블리 셀러스퀘어</a></td><td>동대문 초행자 Q&amp;A, 용어, 사입 단가 감</td></tr>
<tr><td><a href="https://inblog.ai/sellup" target="_blank">셀업 블로그</a></td><td>연휴 일정 공지, 사입 강의</td></tr>
</tbody></table></div>
""")

# ---------------------------------------------------------------- 출처
with tab_src:
    block("""
<h2>출처</h2>
<ol class="sub">
<li><a href="https://montips.com/dongdaemun-market-hours/" target="_blank">montips, 동대문 도매시장 영업시간 총정리 (2026-07)</a></li>
<li><a href="https://montips.com/dongdaemun-wholesale-guide/" target="_blank">montips, 동대문 도매시장 처음 가는 사람을 위한 가이드 (2026-07)</a></li>
<li><a href="https://square.a-bly.com/tipsbeginner-3" target="_blank">에이블리 셀러스퀘어, 동대문 초행자 Q&amp;A</a> · <a href="https://square.a-bly.com/tipsbeginner-1" target="_blank">온라인 vs 오프라인 사입</a></li>
<li><a href="https://www.tosspayments.com/blog/articles/22210" target="_blank">토스페이먼츠, 동대문 시장 기초 정보</a></li>
<li><a href="https://mediahub.seoul.go.kr/archives/2014157" target="_blank">내 손안에 서울, DDP 쇼룸 이용후기</a> · <a href="https://www.hankyung.com/article/202506106292i" target="_blank">한국경제, DDP 쇼룸 1년</a></li>
<li><a href="https://inblog.ai/hanjang/%EB%8F%99%EB%8C%80%EB%AC%B8-%EC%82%AC%EC%9E%85%EC%82%BC%EC%B4%8C-%EC%99%84%EB%B2%BD-%EA%B0%80%EC%9D%B4%EB%93%9C-%EC%87%BC%ED%95%91%EB%AA%B0-%EC%82%AC%EC%9E%A5%EB%8B%98%EC%9D%84-%EC%9C%84%ED%95%9C-%ED%95%84%EC%88%98-%EC%A0%95%EB%B3%B4-8267" target="_blank">한장 블로그, 사입삼촌 가이드 (2023-12)</a></li>
<li><a href="https://m.apparelnews.co.kr/news/news_view/?idx=179142" target="_blank">어패럴뉴스, 동대문 도매 중개 플랫폼 (2019-10)</a></li>
<li><a href="https://www.ktnews.com/news/articleView.html?idxno=132614" target="_blank">한국섬유신문, 링크샵스 폐업</a></li>
<li><a href="https://whereisyourprofit.com/%EB%8F%99%EB%8C%80%EB%AC%B8-%EB%8F%84%EB%A7%A4-%EC%95%88%EB%82%B4%EC%9E%90%EB%A3%8C/" target="_blank">WIYP, 동대문 도매 안내 자료 (디오트 위치)</a></li>
<li><a href="https://imweb.me/blog?idx=491" target="_blank">아임웹, 통신판매업 신고 방법 (2026)</a> · <a href="https://news.jkn.co.kr/post/1061304" target="_blank">재경일보, 온라인 쇼핑몰 시작법</a></li>
</ol>
<p class="note">이 페이지는 공개 자료를 요약한 것이며 상가·플랫폼과 관계없습니다.</p>
""")
