(window._iconfont_svg_string_4641823 =
  '<svg><symbol id="icon-kuake" viewBox="0 0 1024 1024"><path d="M0 0h1024v1024H0z" fill="#000000" fill-opacity="0" ></path><path d="M512 128c180.608 0 326.72 141.888 340.672 320A221.888 221.888 0 0 1 960 638.72c0 121.088-96.32 221.312-217.792 221.312h-40.064a58.624 58.624 0 0 1-7.232-0.192 36.096 36.096 0 0 1-6.144 0.512H281.792v-0.32C160.32 860.032 64 759.808 64 638.784c0-88.384 51.392-165.696 126.4-200.96C201.664 233.792 370.88 128 512 128zM281.792 534.4c-54.528 0-100.928 45.504-100.928 104.32 0 57.472 44.096 102.208 96.832 104.384l4.096 0.064c2.112 0 4.16 0.128 6.208 0.32h220.352a291.712 291.712 0 0 1-7.616-10.048l-15.872-21.824A2175.552 2175.552 0 0 0 412.288 618.24l-6.4-7.808c-40.96-49.856-78.208-76.16-124.096-76.16zM512 244.8c-84.352 0-183.296 58.816-202.112 174.272 81.792 9.856 139.648 61.568 182.336 112.384l3.968 4.736c32.32 39.36 55.04 68.608 75.392 96.128l12.032 16.32 11.904 16.32a256 256 0 0 0 50.24 50.688c21.44 16.256 41.408 25.408 57.216 27.52h39.232c54.528 0 100.928-45.568 100.928-104.448a104.32 104.32 0 0 0-67.712-98.624l-4.032-1.344a58.432 58.432 0 0 1-35.2-81.28C727.04 337.536 629.12 244.864 512 244.864z" fill="#2553F5" ></path></symbol></svg>'),
  (function (n) {
    var t = (t = document.getElementsByTagName("script"))[t.length - 1],
      e = t.getAttribute("data-injectcss"),
      t = t.getAttribute("data-disable-injectsvg");
    if (!t) {
      var i,
        o,
        c,
        a,
        d,
        l = function (t, e) {
          e.parentNode.insertBefore(t, e);
        };
      if (e && !n.__iconfont__svg__cssinject__) {
        n.__iconfont__svg__cssinject__ = !0;
        try {
          document.write(
            "<style>.svgfont {display: inline-block;width: 1em;height: 1em;fill: currentColor;vertical-align: -0.1em;font-size:16px;}</style>"
          );
        } catch (t) {
          console && console.log(t);
        }
      }
      (i = function () {
        var t,
          e = document.createElement("div");
        (e.innerHTML = n._iconfont_svg_string_4641823),
          (e = e.getElementsByTagName("svg")[0]) &&
            (e.setAttribute("aria-hidden", "true"),
            (e.style.position = "absolute"),
            (e.style.width = 0),
            (e.style.height = 0),
            (e.style.overflow = "hidden"),
            (e = e),
            (t = document.body).firstChild
              ? l(e, t.firstChild)
              : t.appendChild(e));
      }),
        document.addEventListener
          ? ~["complete", "loaded", "interactive"].indexOf(document.readyState)
            ? setTimeout(i, 0)
            : ((o = function () {
                document.removeEventListener("DOMContentLoaded", o, !1), i();
              }),
              document.addEventListener("DOMContentLoaded", o, !1))
          : document.attachEvent &&
            ((c = i),
            (a = n.document),
            (d = !1),
            r(),
            (a.onreadystatechange = function () {
              "complete" == a.readyState &&
                ((a.onreadystatechange = null), s());
            }));
    }
    function s() {
      d || ((d = !0), c());
    }
    function r() {
      try {
        a.documentElement.doScroll("left");
      } catch (t) {
        return void setTimeout(r, 50);
      }
      s();
    }
  })(window);
