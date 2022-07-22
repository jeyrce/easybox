FROM --platform=linux/amd64 nginx:1.22.0-alpine
LABEL Author='Jeyrce Lu<jeyrce@gmail.com>' \
      Repo='https://github.com/jeyrce/easybox'
ENV WEB_TITLE='数据分发'
ENV WEB_DOMAIN='xoo.site'
ENV WEB_ICP='浙ICP备18053740号-3'
ENV POST_TITLE='《青春》'
ENV POST_CONTENT=" \
    青春不是年华，而是心境；青春不是桃面、丹唇、柔膝，而是深沉的意志、恢宏的想象、炽热的感情；\
    青春是生命的深泉在涌流。\
    \
    青春气贯长虹，勇锐盖过怯弱，进取压倒苟安。如此锐气，二十后生有之，六旬男子则更多见。\
    年岁有加，并非垂老，理想丢弃，方堕暮年。 \
    \
    岁月悠悠，衰微只及肌肤；热忱抛却，颓唐必至灵魂。\
    忧烦、惶恐、丧失自信，定使心灵扭曲，意气如灰。\
    \
    无论年届花甲，抑或二八芳龄，心中皆有生命之欢乐，奇迹之诱惑，孩童般天真久盛不衰。\
    \
    人心中皆有一台天线，只要你从天上人间接受美好、希望、欢乐、勇气和力量的信号，你就青春永驻、风华长存。\
    \
    一旦天线降下，锐气便被冰雪覆盖，玩世不恭、自暴自弃油然而生，即便年方二十，实已垂垂老矣；\
    然则只要竖起天线，捕捉乐观信号，你就有望在八十高龄告别尘寰时仍觉年轻。\
"
WORKDIR /index
COPY nginx.conf /etc/nginx/nginx.conf
COPY docker-entrypoint.sh /
COPY . .
RUN rm -rf /docker-entrypoint.d/

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 80

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]
