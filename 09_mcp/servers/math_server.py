"""두 수를 더하는 Tool을 제공하는 MCP Server"""

from mcp.server import MCPServer

# "math_tools"라는 이름을 갖는 MCP Server 인스턴스를 생성
# - Host(AI 클라이언트 == Claude Code, Codex, Pycharm 등) 호스트 연결 시 노출되는
#   Tools, Resources, Prompt를 등록하고 관리하는 역할을 함
mcp = MCPServer("math_tools")

@mcp.tool()        # 해당 함수를 MCP Tool 규격으로 자동 변환
                   # () 내 "도구명"을 적지 않으면 함수명이 도구명이 된다.
def add(a: float, b: float) -> float:
    """두 숫자 a 와 b를 받아 두 수를 더한 후 10을 곱해 반환한다."""
    return (a + b) * 10

@mcp.tool()        # 해당 함수를 MCP Tool 규격으로 자동 변환
                   # () 내 "도구명"을 적지 않으면 함수명이 도구명이 된다.
def minus(a: float, b: float) -> float:
    """두 숫자 a 와 b를 받아 두 수를 뺀 후 제곱해 반환한다."""
    return (a - b)  ** 2

# 현재 py 파일이 실행중인 상태라면
if __name__ == "__main__":
    try:
        mcp.run(
            transport="streamable-http",
            host = "127.0.0.1", # 서버주소
            port = 8001, # 웹요청 시 프로그램 구분 번호
            streamable_http_path = "/mcp" # 나머지 주소
        )
    except KeyboardInterrupt:
    # CTRL + C (종료) 시 SDK가 다시 실행하려는 메시지 숨기기
        pass
