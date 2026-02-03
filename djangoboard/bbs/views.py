from django.shortcuts import render

# Create your views here.
def post_list(request):
  dummy_posts = [
    {
      "title": "はじめてのDjango",
      "author_name": "山田",
      "created_at": "2026-02-03 19:10",
      "body": "URL → View → Template の流れが分かってきました。",
    },
    {
      "title": "テンプレ継承が便利",
      "author_name": "佐藤",
      "created_at": "2026-02-03 19:20",
      "body": "base.html を作ると全ページの見た目が揃って楽ですね。",
    },
    {
      "title": "staticでCSSを当てる",
      "author_name": "鈴木",
      "created_at": "2026-02-03 19:30",
      "body": "CSSを当てたら一気にサイトっぽくなりました！",
    },
  ]

  return render(
    request,
    "bbs/post_list.html",
    {
      #変数をテンプレートに渡す
      "page_title": "BBS 投稿一覧",
      "posts": dummy_posts,
    }
  )

def about(request):
  return render(
    request,
    "bbs/about.html",
    {
      #変数をテンプレートに渡す
      "page_title": "BBS このサイトについて",
    }
  )