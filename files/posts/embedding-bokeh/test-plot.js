(function() {
  const fn = function() {
    (function(root) {
      function now() {
        return new Date();
      }
    
      const force = false;
    
      if (typeof root._bokeh_onload_callbacks === "undefined" || force === true) {
        root._bokeh_onload_callbacks = [];
        root._bokeh_is_loading = undefined;
      }
    
    
    const element = document.getElementById("af99effb-d79b-4f6e-84aa-0af5e1a98d54");
        if (element == null) {
          console.warn("Bokeh: autoload.js configured with elementid 'af99effb-d79b-4f6e-84aa-0af5e1a98d54' but no matching script tag was found.")
        }
      function run_callbacks() {
        try {
          root._bokeh_onload_callbacks.forEach(function(callback) {
            if (callback != null)
              callback();
          });
        } finally {
          delete root._bokeh_onload_callbacks
        }
        console.debug("Bokeh: all callbacks have finished");
      }
    
      function load_libs(css_urls, js_urls, callback) {
        if (css_urls == null) css_urls = [];
        if (js_urls == null) js_urls = [];
    
        root._bokeh_onload_callbacks.push(callback);
        if (root._bokeh_is_loading > 0) {
          console.debug("Bokeh: BokehJS is being loaded, scheduling callback at", now());
          return null;
        }
        if (js_urls == null || js_urls.length === 0) {
          run_callbacks();
          return null;
        }
        console.debug("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
        root._bokeh_is_loading = css_urls.length + js_urls.length;
    
        function on_load() {
          root._bokeh_is_loading--;
          if (root._bokeh_is_loading === 0) {
            console.debug("Bokeh: all BokehJS libraries/stylesheets loaded");
            run_callbacks()
          }
        }
    
        function on_error(url) {
          console.error("failed to load " + url);
        }
    
        for (let i = 0; i < css_urls.length; i++) {
          const url = css_urls[i];
          const element = document.createElement("link");
          element.onload = on_load;
          element.onerror = on_error.bind(null, url);
          element.rel = "stylesheet";
          element.type = "text/css";
          element.href = url;
          console.debug("Bokeh: injecting link tag for BokehJS stylesheet: ", url);
          document.body.appendChild(element);
        }
    
        for (let i = 0; i < js_urls.length; i++) {
          const url = js_urls[i];
          const element = document.createElement('script');
          element.onload = on_load;
          element.onerror = on_error.bind(null, url);
          element.async = false;
          element.src = url;
          console.debug("Bokeh: injecting script tag for BokehJS library: ", url);
          document.head.appendChild(element);
        }
      };
    
      function inject_raw_css(css) {
        const element = document.createElement("style");
        element.appendChild(document.createTextNode(css));
        document.body.appendChild(element);
      }
    
      const js_urls = ["https://cdn.bokeh.org/bokeh/release/bokeh-2.4.3.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-gl-2.4.3.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-widgets-2.4.3.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-tables-2.4.3.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-mathjax-2.4.3.min.js", "https://unpkg.com/@holoviz/panel@0.14.4/dist/panel.min.js"];
      const css_urls = [];
    
      const inline_js = [    function(Bokeh) {
          Bokeh.set_log_level("info");
        },
        function(Bokeh) {
          (function() {
            const fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                  const docs_json = '{"2396b19e-970f-4cd3-926f-9874a83f06db":{"defs":[{"extends":null,"module":null,"name":"ReactiveHTML1","overrides":[],"properties":[]},{"extends":null,"module":null,"name":"FlexBox1","overrides":[],"properties":[{"default":"flex-start","kind":null,"name":"align_content"},{"default":"flex-start","kind":null,"name":"align_items"},{"default":"row","kind":null,"name":"flex_direction"},{"default":"wrap","kind":null,"name":"flex_wrap"},{"default":"flex-start","kind":null,"name":"justify_content"}]},{"extends":null,"module":null,"name":"GridStack1","overrides":[],"properties":[{"default":"warn","kind":null,"name":"mode"},{"default":null,"kind":null,"name":"ncols"},{"default":null,"kind":null,"name":"nrows"},{"default":true,"kind":null,"name":"allow_resize"},{"default":true,"kind":null,"name":"allow_drag"},{"default":[],"kind":null,"name":"state"}]},{"extends":null,"module":null,"name":"click1","overrides":[],"properties":[{"default":"","kind":null,"name":"terminal_output"},{"default":"","kind":null,"name":"debug_name"},{"default":0,"kind":null,"name":"clears"}]},{"extends":null,"module":null,"name":"NotificationAreaBase1","overrides":[],"properties":[{"default":"bottom-right","kind":null,"name":"position"},{"default":0,"kind":null,"name":"_clear"}]},{"extends":null,"module":null,"name":"NotificationArea1","overrides":[],"properties":[{"default":[],"kind":null,"name":"notifications"},{"default":"bottom-right","kind":null,"name":"position"},{"default":0,"kind":null,"name":"_clear"},{"default":[{"background":"#ffc107","icon":{"className":"fas fa-exclamation-triangle","color":"white","tagName":"i"},"type":"warning"},{"background":"#007bff","icon":{"className":"fas fa-info-circle","color":"white","tagName":"i"},"type":"info"}],"kind":null,"name":"types"}]},{"extends":null,"module":null,"name":"Notification","overrides":[],"properties":[{"default":null,"kind":null,"name":"background"},{"default":3000,"kind":null,"name":"duration"},{"default":null,"kind":null,"name":"icon"},{"default":"","kind":null,"name":"message"},{"default":null,"kind":null,"name":"notification_type"},{"default":false,"kind":null,"name":"_destroyed"}]},{"extends":null,"module":null,"name":"TemplateActions1","overrides":[],"properties":[{"default":0,"kind":null,"name":"open_modal"},{"default":0,"kind":null,"name":"close_modal"}]},{"extends":null,"module":null,"name":"MaterialTemplateActions1","overrides":[],"properties":[{"default":0,"kind":null,"name":"open_modal"},{"default":0,"kind":null,"name":"close_modal"}]}],"roots":{"references":[{"attributes":{"source":{"id":"7808"}},"id":"7813","type":"CDSView"},{"attributes":{"below":[{"id":"7786"}],"center":[{"id":"7789"},{"id":"7793"}],"left":[{"id":"7790"}],"renderers":[{"id":"7812"}],"sizing_mode":"stretch_width","title":{"id":"7776"},"toolbar":{"id":"7801"},"x_range":{"id":"7778"},"x_scale":{"id":"7782"},"y_range":{"id":"7780"},"y_scale":{"id":"7784"}},"id":"7775","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"7821","type":"UnionRenderers"},{"attributes":{},"id":"7778","type":"DataRange1d"},{"attributes":{"coordinates":null,"data_source":{"id":"7808"},"glyph":{"id":"7809"},"group":null,"hover_glyph":null,"muted_glyph":{"id":"7811"},"nonselection_glyph":{"id":"7810"},"view":{"id":"7813"}},"id":"7812","type":"GlyphRenderer"},{"attributes":{},"id":"7791","type":"BasicTicker"},{"attributes":{},"id":"7822","type":"Selection"},{"attributes":{"coordinates":null,"formatter":{"id":"7816"},"group":null,"major_label_policy":{"id":"7817"},"ticker":{"id":"7791"}},"id":"7790","type":"LinearAxis"},{"attributes":{},"id":"7819","type":"BasicTickFormatter"},{"attributes":{},"id":"7799","type":"HelpTool"},{"attributes":{},"id":"7820","type":"AllLabels"},{"attributes":{"line_color":"#1f77b4","x":{"field":"x"},"y":{"field":"y"}},"id":"7809","type":"Line"},{"attributes":{"overlay":{"id":"7800"}},"id":"7796","type":"BoxZoomTool"},{"attributes":{"coordinates":null,"formatter":{"id":"7819"},"group":null,"major_label_policy":{"id":"7820"},"ticker":{"id":"7787"}},"id":"7786","type":"LinearAxis"},{"attributes":{},"id":"7817","type":"AllLabels"},{"attributes":{"tools":[{"id":"7794"},{"id":"7795"},{"id":"7796"},{"id":"7797"},{"id":"7798"},{"id":"7799"}]},"id":"7801","type":"Toolbar"},{"attributes":{},"id":"7795","type":"WheelZoomTool"},{"attributes":{"axis":{"id":"7786"},"coordinates":null,"group":null,"ticker":null},"id":"7789","type":"Grid"},{"attributes":{},"id":"7782","type":"LinearScale"},{"attributes":{"data":{"x":[1,2,3],"y":[4,1,2]},"selected":{"id":"7822"},"selection_policy":{"id":"7821"}},"id":"7808","type":"ColumnDataSource"},{"attributes":{},"id":"7784","type":"LinearScale"},{"attributes":{},"id":"7797","type":"SaveTool"},{"attributes":{"axis":{"id":"7790"},"coordinates":null,"dimension":1,"group":null,"ticker":null},"id":"7793","type":"Grid"},{"attributes":{},"id":"7794","type":"PanTool"},{"attributes":{},"id":"7787","type":"BasicTicker"},{"attributes":{},"id":"7798","type":"ResetTool"},{"attributes":{"coordinates":null,"group":null,"text":"Plot Title"},"id":"7776","type":"Title"},{"attributes":{},"id":"7780","type":"DataRange1d"},{"attributes":{},"id":"7816","type":"BasicTickFormatter"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","x":{"field":"x"},"y":{"field":"y"}},"id":"7810","type":"Line"},{"attributes":{"bottom_units":"screen","coordinates":null,"fill_alpha":0.5,"fill_color":"lightgrey","group":null,"left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"right_units":"screen","syncable":false,"top_units":"screen"},"id":"7800","type":"BoxAnnotation"},{"attributes":{"line_alpha":0.2,"line_color":"#1f77b4","x":{"field":"x"},"y":{"field":"y"}},"id":"7811","type":"Line"}],"root_ids":["7775"]},"title":"Bokeh Application","version":"2.4.3"}}';
                  const render_items = [{"docid":"2396b19e-970f-4cd3-926f-9874a83f06db","root_ids":["7775"],"roots":{"7775":"af99effb-d79b-4f6e-84aa-0af5e1a98d54"}}];
                  root.Bokeh.embed.embed_items(docs_json, render_items);
                  }
                  if (root.Bokeh !== undefined) {
                    embed_document(root);
                  } else {
                    let attempts = 0;
                    const timer = setInterval(function(root) {
                      if (root.Bokeh !== undefined) {
                        clearInterval(timer);
                        embed_document(root);
                      } else {
                        attempts++;
                        if (attempts > 100) {
                          clearInterval(timer);
                          console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                        }
                      }
                    }, 10, root)
                  }
                })(window);
              });
            };
            if (document.readyState != "loading") fn();
            else document.addEventListener("DOMContentLoaded", fn);
          })();
        },
    function(Bokeh) {
        }
      ];
    
      function run_inline_js() {
        for (let i = 0; i < inline_js.length; i++) {
          inline_js[i].call(root, root.Bokeh);
        }
      }
    
      if (root._bokeh_is_loading === 0) {
        console.debug("Bokeh: BokehJS loaded, going straight to plotting");
        run_inline_js();
      } else {
        load_libs(css_urls, js_urls, function() {
          console.debug("Bokeh: BokehJS plotting callback run at", now());
          run_inline_js();
        });
      }
    }(window));
  };
  if (document.readyState != "loading") fn();
  else document.addEventListener("DOMContentLoaded", fn);
})();