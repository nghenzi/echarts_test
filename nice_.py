from panel.layout.base import WidgetBox
from bokeh.plotting import figure
from bokeh.models import WMTSTileSource, BBoxTileSource, QUADKEYTileSource
p = figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000), width=400, height=300,
           x_axis_type="mercator", y_axis_type="mercator", sizing_mode='stretch_both')
p.grid.grid_line_alpha = 0.1
p.toolbar_location = None
p.border_fill_color = None
p.axis.visible = False
p.add_tile(WMTSTileSource(url='https://cartodb-basemaps-4.global.ssl.fastly.net/dark_all/{Z}/{X}/{Y}.png'))


import param, pandas as pd
from panel.reactive import ReactiveHTML
from datetime import date

class MaterialTextField(ReactiveHTML):
    
    value = param.String(default='')
    
    _template = """
<div style="width:400px" id='text_field' class="mdc-text-field mdc-text-field--outlined mdc-text-field--with-leading-icon mdc-text-field--with-trailing-icon">
  <i class="material-icons mdc-text-field__icon">favorite</i>
  <i class="material-icons mdc-text-field__icon">visibility</i>
  <input class="mdc-text-field__input" id="text-field-hero-input"/>
  <div class="mdc-notched-outline">
    <div class="mdc-notched-outline__leading"></div>
    <div class="mdc-notched-outline__notch">
      <label for="text-field-hero-input" class="mdc-floating-label">Name</label>
    </div>
    <div class="mdc-notched-outline__trailing"></div>
  </div>
</div>
    """

    
    
    _dom_events = {'text-input': ['change']}
    
    _scripts = {
        'render': "mdc.textField.MDCTextField.attachTo(text_field);"
    }
    
    __javascript__ = [
        'https://unpkg.com/material-components-web@latest/dist/material-components-web.min.js'
    ]
    
    __css__ = [
        'https://unpkg.com/material-components-web@latest/dist/material-components-web.min.css'
    ]
    
text_field = MaterialTextField(
                    margin=(16,0,0,0))


import panel as pn

css = """

.drag_content{
    position: fixed;
    visibility: hidden;
    z-index: 9999999999;
    padding: 0px;
    border-radius: 5px;

    border: 1px solid;
  padding: 10px;
  box-shadow: 3px 5px #888888;
}


.drag_icon .tooltiptext {
    position: static;
    visibility: hidden;
    width: 120px;
    height: 15px
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;
    position: absolute;
    z-index: 1000000;
    bottom: -99%;
    left: 25%;
    margin-left: -60px;
    opacity: 0;
    transition: opacity 0.3s;
  }  

.drag_icon:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
  }

.bk-root{ /*vanilla template */
    z-index: inherit;
}

#header-items { /* fast list template */
  z-index: 999999999;
}

#header{
 z-index: 999999999;
}

.drag-handle {
     /* style="position:relative; left:20px; top:25px; */
    /*  z-index:999999999;" */
    position: absolute;
    top: 5px;
    left: 5px;
    width: 24px;
    height: 24px;
    z-index: 1000000000000000;
    background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48cGF0aCBmaWxsPSJub25lIiBkPSJNMCAwaDI0djI0SDB6Ii8+PHBhdGggZD0iTTE2IDEzbDYuOTY0IDQuMDYyLTIuOTczLjg1IDIuMTI1IDMuNjgxLTEuNzMyIDEtMi4xMjUtMy42OC0yLjIyMyAyLjE1TDE2IDEzem0tMi03aDJ2Mmg1YTEgMSAwIDAgMSAxIDF2NGgtMnYtM0gxMHYxMGg0djJIOWExIDEgMCAwIDEtMS0xdi01SDZ2LTJoMlY5YTEgMSAwIDAgMSAxLTFoNVY2ek00IDE0djJIMnYtMmgyem0wLTR2Mkgydi0yaDJ6bTAtNHYySDJWNmgyem0wLTR2MkgyVjJoMnptNCAwdjJINlYyaDJ6bTQgMHYyaC0yVjJoMnptNCAwdjJoLTJWMmgyeiIvPjwvc3ZnPg==');
    opacity: 0;
    transition-delay: 0.5s;
    transition: 0.5s;
  }
  
  .drag-handle:hover {
    transition: 0.5s;
    opacity: 1;
  }
  
  .drag-handle:focus {
    opacity: 1;
  }
  

  .drag-handle-dark {
    /* style="position:relative; left:20px; top:25px; */
   /*  z-index:999999999;" */
   position: absolute;
   top: 25px;
   left: 20px;
   width: 24px;
   height: 24px;
   z-index: 1000000000000000;
   background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48cGF0aCBmaWxsPSJub25lIiBkPSJNMCAwaDI0djI0SDB6Ii8+PHBhdGggZD0iTTE2IDEzbDYuOTY0IDQuMDYyLTIuOTczLjg1IDIuMTI1IDMuNjgxLTEuNzMyIDEtMi4xMjUtMy42OC0yLjIyMyAyLjE1TDE2IDEzem0tMi03aDJ2Mmg1YTEgMSAwIDAgMSAxIDF2NGgtMnYtM0gxMHYxMGg0djJIOWExIDEgMCAwIDEtMS0xdi01SDZ2LTJoMlY5YTEgMSAwIDAgMSAxLTFoNVY2ek00IDE0djJIMnYtMmgyem0wLTR2Mkgydi0yaDJ6bTAtNHYySDJWNmgyem0wLTR2MkgyVjJoMnptNCAwdjJINlYyaDJ6bTQgMHYyaC0yVjJoMnptNCAwdjJoLTJWMmgyeiIvPjwvc3ZnPg==');
   opacity: 0;
   transition-delay: 0.5s;
   transition: 0.5s;
   filter: invert(1);
 }
 
 .drag-handle-dark:hover {
   transition: 0.5s;
   opacity: 1;
 }
 
 .drag-handle-dark:focus {
   opacity: 1;
 }


.drag_icon {
    display: inline-block;
    vertical-align: middle;
    transform: translateZ(0);
    box-shadow: 0 0 1px rgba(0, 0, 0, 0);
    backface-visibility: hidden;
    -moz-osx-font-smoothing: grayscale;
    transition-duration: 0.3s;
    transition-property: transform;
}

.drag_icon:hover,
.drag_icon:focus,
.drag_icon:active {
    transform: scale(1.);
}

.drag_icon {
  background-color: transparent;
  border-radius: 50%;
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  overflow: hidden;
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: color, background-color;
  transition-property: color, background-color;
}
.drag_icon:hover, .drag_icon:focus, .drag_icon:active {
  background-color: transparent;//#2098D1;
  border-radius: 50%;
  color: white;
  font-weight:bold;
}

.drag_icon:hover, .drag_icon:focus, .drag_icon:active {
  background-color: transparent;//#2098D1;
  border-radius: 50%;
  font-weight: 900 !important;
  color: white;
}

.bk-root .noUi-connect {
    background-color: rgb(80 100 165) !important;
}

.card_col {
 background-color: #3f51b569;
 border-radius:5px;

}

.icon_bar{
    background-color: #2f2f31;
    color:white;
}

body {
  margin: 0
}

.header_bar{
   border: 0 !important;
    height: 5px !important;
    background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)) !important;
    background-image: -moz-linear-gradient(left, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)) !important;
    background-image: -ms-linear-gradient(left, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)) !important;
    background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)) !important;
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffff', endColorstr='#000000', GradientType=1) !important;
}

html, body {margin: 0; height: 100%;  position: fixed; background-color: white;}
"""  

css_file = ['https://fonts.googleapis.com/icon?family=Material+Icons']

pn.extension(raw_css=[css], css_files = css_file)


class Link(pn.reactive.ReactiveHTML):
    
    click = param.Integer(default=0)
    
    _template = """<a id="a" target="_blank" onclick="${script('update_click')}" href="https://www.w3schools.com">Visit W3Schools.com!</a>"""
    
    _scripts = {
        "update_click": """
            data.click = data.click+1
            console.log(data.click)
        """
    }
    
    
toggle =pn.widgets.Toggle(value=False)
link = Link()
link.jscallback(args={"toggle": toggle}, click="toggle.active = (source.click>0)")

linu  = pn.Column(toggle, link, height=200)
import numpy as np

def get_figure():
    x = np.linspace(0.1, 5, 80)

    p = figure(title="log axis example", y_axis_type="log",
            x_range=(0, 5), y_range=(0.001, 10**22), sizing_mode = 'stretch_both',
            background_fill_color="#fafafa")

    p.border_fill_color = None
    p.line(x, np.sqrt(x), legend_label="y=sqrt(x)",
        line_color="tomato", line_dash="dashed")

    p.line(x, x, legend_label="y=x")
    p.circle(x, x, legend_label="y=x")

    p.line(x, x**2, legend_label="y=x**2")
    p.circle(x, x**2, legend_label="y=x**2",
            fill_color=None, line_color="olivedrab")

    p.line(x, 10**x, legend_label="y=10^x",
        line_color="gold", line_width=2)

    p.line(x, x**x, legend_label="y=x^x",
        line_dash="dotted", line_color="indigo", line_width=2)

    p.line(x, 10**(x**2), legend_label="y=10^(x^2)",
        line_color="coral", line_dash="dotdash", line_width=2)

    p.xaxis.major_label_text_font_size = '16pt'    
    p.yaxis.major_label_text_font_size = '16pt'
    p.legend.location = "top_left"

    return pn.pane.Bokeh(p, margin=10)




def colorce():
    import colorcet as cc
    from numpy import linspace
    from scipy.stats.kde import gaussian_kde

    from bokeh.io import output_file, show
    from bokeh.models import ColumnDataSource, FixedTicker, PrintfTickFormatter
    from bokeh.plotting import figure
    from bokeh.sampledata.perceptions import probly

    output_file("ridgeplot.html")

    def ridge(category, data, scale=20):
        return list(zip([category]*len(data), scale*data))

    cats = list(reversed(probly.keys()))

    palette = [cc.rainbow[i*15] for i in range(17)]

    x = linspace(-20,110, 500)

    source = ColumnDataSource(data=dict(x=x))

    p = figure(y_range=cats, plot_width=900, x_range=(-5, 105), toolbar_location=None)

    for i, cat in enumerate(reversed(cats)):
        pdf = gaussian_kde(probly[cat])
        y = ridge(cat, pdf(x))
        source.add(y, cat)
        p.patch('x', cat, color=palette[i], alpha=0.6, line_color="black", source=source)

    p.outline_line_color = None
    p.background_fill_color = "#efefef"

    p.xaxis.ticker = FixedTicker(ticks=list(range(0, 101, 10)))
    p.xaxis.formatter = PrintfTickFormatter(format="%d%%")

    p.ygrid.grid_line_color = None
    p.xgrid.grid_line_color = "#dddddd"
    p.xgrid.ticker = p.xaxis.ticker

    p.axis.minor_tick_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.axis_line_color = None

    p.y_range.range_padding = 0.12
    return p

p123 = colorce()

p21 = get_figure()

svg_favicon = """ <svg width="128" height="128" xmlns="http://www.w3.org/2000/svg">
  <style>
    path { fill: #000000; }
    @media (prefers-color-scheme: dark) {
      path { fill: #ffffff; }
    }
  </style>
  <path d="M111.904 52.937a1.95 1.95 0 00-1.555-1.314l-30.835-4.502-13.786-28.136c-.653-1.313-2.803-1.313-3.456 0L48.486 47.121l-30.835 4.502a1.95 1.95 0 00-1.555 1.314 1.952 1.952 0 00.48 1.99l22.33 21.894-5.28 30.918c-.115.715.173 1.45.768 1.894a1.904 1.904 0 002.016.135L64 95.178l27.59 14.59c.269.155.576.232.883.232a1.98 1.98 0 001.133-.367 1.974 1.974 0 00.768-1.894l-5.28-30.918 22.33-21.893c.518-.522.71-1.276.48-1.99z" fill-rule="nonzero"/>
</svg>"""


h, color = 70, '#8e8e94'
svg_vsc = f""" <svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 48 48" width="{h}px" height="{h}px"><path fill="#29b6f6" d="M44,11.11v25.78c0,1.27-0.79,2.4-1.98,2.82l-8.82,4.14L34,33V15L33.2,4.15l8.82,4.14 C43.21,8.71,44,9.84,44,11.11z"/><path fill="#0277bd" d="M9,33.896L34,15V5.353c0-1.198-1.482-1.758-2.275-0.86L4.658,29.239 c-0.9,0.83-0.849,2.267,0.107,3.032c0,0,1.324,1.232,1.803,1.574C7.304,34.37,8.271,34.43,9,33.896z"/><path fill="#0288d1" d="M9,14.104L34,33v9.647c0,1.198-1.482,1.758-2.275,0.86L4.658,18.761 c-0.9-0.83-0.849-2.267,0.107-3.032c0,0,1.324-1.232,1.803-1.574C7.304,13.63,8.271,13.57,9,14.104z"/></svg>"""
svg_settings = f"""<svg xmlns="http://www.w3.org/2000/svg" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M19.43 12.98c.04-.32.07-.64.07-.98 0-.34-.03-.66-.07-.98l2.11-1.65c.19-.15.24-.42.12-.64l-2-3.46c-.09-.16-.26-.25-.44-.25-.06 0-.12.01-.17.03l-2.49 1c-.52-.4-1.08-.73-1.69-.98l-.38-2.65C14.46 2.18 14.25 2 14 2h-4c-.25 0-.46.18-.49.42l-.38 2.65c-.61.25-1.17.59-1.69.98l-2.49-1c-.06-.02-.12-.03-.18-.03-.17 0-.34.09-.43.25l-2 3.46c-.13.22-.07.49.12.64l2.11 1.65c-.04.32-.07.65-.07.98 0 .33.03.66.07.98l-2.11 1.65c-.19.15-.24.42-.12.64l2 3.46c.09.16.26.25.44.25.06 0 .12-.01.17-.03l2.49-1c.52.4 1.08.73 1.69.98l.38 2.65c.03.24.24.42.49.42h4c.25 0 .46-.18.49-.42l.38-2.65c.61-.25 1.17-.59 1.69-.98l2.49 1c.06.02.12.03.18.03.17 0 .34-.09.43-.25l2-3.46c.12-.22.07-.49-.12-.64l-2.11-1.65zm-1.98-1.71c.04.31.05.52.05.73 0 .21-.02.43-.05.73l-.14 1.13.89.7 1.08.84-.7 1.21-1.27-.51-1.04-.42-.9.68c-.43.32-.84.56-1.25.73l-1.06.43-.16 1.13-.2 1.35h-1.4l-.19-1.35-.16-1.13-1.06-.43c-.43-.18-.83-.41-1.23-.71l-.91-.7-1.06.43-1.27.51-.7-1.21 1.08-.84.89-.7-.14-1.13c-.03-.31-.05-.54-.05-.74s.02-.43.05-.73l.14-1.13-.89-.7-1.08-.84.7-1.21 1.27.51 1.04.42.9-.68c.43-.32.84-.56 1.25-.73l1.06-.43.16-1.13.2-1.35h1.39l.19 1.35.16 1.13 1.06.43c.43.18.83.41 1.23.71l.91.7 1.06-.43 1.27-.51.7 1.21-1.07.85-.89.7.14 1.13zM12 8c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4zm0 6c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z"/></svg>"""
svg_ar = f"""<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><rect fill="none" height="24" width="24" x="0" y="0"/></g><g><g><path d="M3,4c0-0.55,0.45-1,1-1h2V1H4C2.34,1,1,2.34,1,4v2h2V4z"/><path d="M3,20v-2H1v2c0,1.66,1.34,3,3,3h2v-2H4C3.45,21,3,20.55,3,20z"/><path d="M20,1h-2v2h2c0.55,0,1,0.45,1,1v2h2V4C23,2.34,21.66,1,20,1z"/><path d="M21,20c0,0.55-0.45,1-1,1h-2v2h2c1.66,0,3-1.34,3-3v-2h-2V20z"/><path d="M19,14.87V9.13c0-0.72-0.38-1.38-1-1.73l-5-2.88c-0.31-0.18-0.65-0.27-1-0.27s-0.69,0.09-1,0.27L6,7.39 C5.38,7.75,5,8.41,5,9.13v5.74c0,0.72,0.38,1.38,1,1.73l5,2.88c0.31,0.18,0.65,0.27,1,0.27s0.69-0.09,1-0.27l5-2.88 C18.62,16.25,19,15.59,19,14.87z M11,17.17l-4-2.3v-4.63l4,2.33V17.17z M12,10.84L8.04,8.53L12,6.25l3.96,2.28L12,10.84z M17,14.87l-4,2.3v-4.6l4-2.33V14.87z"/></g></g></svg>"""
svg_table = f"""<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><rect fill="none" height="24" width="24"/><path d="M19,7H9C7.9,7,7,7.9,7,9v10c0,1.1,0.9,2,2,2h10c1.1,0,2-0.9,2-2V9C21,7.9,20.1,7,19,7z M19,9v2H9V9H19z M13,15v-2h2v2H13z M15,17v2h-2v-2H15z M11,15H9v-2h2V15z M17,13h2v2h-2V13z M9,17h2v2H9V17z M17,19v-2h2v2H17z M6,17H5c-1.1,0-2-0.9-2-2V5 c0-1.1,0.9-2,2-2h10c1.1,0,2,0.9,2,2v1h-2V5H5v10h1V17z"/></g></svg>"""
svg_triangle = f""" <svg xmlns="http://www.w3.org/2000/svg" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M17.99 11.57H20V0L0 20h11.56v-2H4.83L17.99 4.83v6.74zm5.78 8.75l-1.07-.83c.02-.16.04-.32.04-.49 0-.17-.01-.33-.04-.49l1.06-.83c.09-.08.12-.21.06-.32l-1-1.73c-.06-.11-.19-.15-.31-.11l-1.24.5c-.26-.2-.54-.37-.85-.49l-.19-1.32c-.01-.12-.12-.21-.24-.21h-2c-.12 0-.23.09-.25.21l-.19 1.32c-.3.13-.59.29-.85.49l-1.24-.5c-.11-.04-.24 0-.31.11l-1 1.73c-.06.11-.04.24.06.32l1.06.83c-.02.16-.03.32-.03.49 0 .17.01.33.03.49l-1.06.83c-.09.08-.12.21-.06.32l1 1.73c.06.11.19.15.31.11l1.24-.5c.26.2.54.37.85.49l.19 1.32c.02.12.12.21.25.21h2c.12 0 .23-.09.25-.21l.19-1.32c.3-.13.59-.29.84-.49l1.25.5c.11.04.24 0 .31-.11l1-1.73c.06-.11.03-.24-.06-.32zm-4.78.18c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>"""
svg_dev = f""" <svg xmlns="http://www.w3.org/2000/svg" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M7 5h10v2h2V3c0-1.1-.9-1.99-2-1.99L7 1c-1.1 0-2 .9-2 2v4h2V5zm8.41 11.59L20 12l-4.59-4.59L14 8.83 17.17 12 14 15.17l1.41 1.42zM10 15.17L6.83 12 10 8.83 8.59 7.41 4 12l4.59 4.59L10 15.17zM17 19H7v-2H5v4c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2v-4h-2v2z"/></svg>"""
svg_drive_file = f""" <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><rect fill="none" height="24" width="24"/></g><g><g><polygon points="15,16 11,20 21,20 21,16"/><path d="M12.06,7.19L3,16.25V20h3.75l9.06-9.06L12.06,7.19z M5.92,18H5v-0.92l7.06-7.06l0.92,0.92L5.92,18z"/><path d="M18.71,8.04c0.39-0.39,0.39-1.02,0-1.41l-2.34-2.34C16.17,4.09,15.92,4,15.66,4c-0.25,0-0.51,0.1-0.7,0.29l-1.83,1.83 l3.75,3.75L18.71,8.04z"/></g></g></svg>"""
svg_logout = f"""<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><path d="M0,0h24v24H0V0z" fill="none"/></g><g><path d="M17,8l-1.41,1.41L17.17,11H9v2h8.17l-1.58,1.58L17,16l4-4L17,8z M5,5h7V3H5C3.9,3,3,3.9,3,5v14c0,1.1,0.9,2,2,2h7v-2H5V5z"/></g></svg>"""

h=45
svg_subject = f"""<svg xmlns="http://www.w3.org/2000/svg" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M14 17H4v2h10v-2zm6-8H4v2h16V9zM4 15h16v-2H4v2zM4 5v2h16V5H4z"/></svg>"""
svg_notif = f"""<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><path d="M0,0h24v24H0V0z" fill="none"/></g><g><path d="M12,18.5c0.83,0,1.5-0.67,1.5-1.5h-3C10.5,17.83,11.17,18.5,12,18.5z M12,2C6.48,2,2,6.48,2,12s4.48,10,10,10 c5.52,0,10-4.48,10-10S17.52,2,12,2z M12,20c-4.41,0-8-3.59-8-8s3.59-8,8-8c4.41,0,8,3.59,8,8S16.41,20,12,20z M16,11.39 c0-2.11-1.03-3.92-3-4.39V6.5c0-0.57-0.43-1-1-1s-1,0.43-1,1V7c-1.97,0.47-3,2.27-3,4.39V14H7v2h10v-2h-1V11.39z M14,14h-4v-3 c0-1.1,0.9-2,2-2s2,0.9,2,2V14z"/></g></svg>"""
svg_mediation = f"""<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><rect fill="none" height="24" width="24"/><path d="M18,16l4-4l-4-4v3h-5.06c-0.34-3.1-2.26-5.72-4.94-7.05C7.96,2.31,6.64,1,5,1C3.34,1,2,2.34,2,4s1.34,3,3,3 c0.95,0,1.78-0.45,2.33-1.14C9.23,6.9,10.6,8.77,10.92,11h-3.1C7.4,9.84,6.3,9,5,9c-1.66,0-3,1.34-3,3s1.34,3,3,3 c1.3,0,2.4-0.84,2.82-2h3.1c-0.32,2.23-1.69,4.1-3.58,5.14C6.78,17.45,5.95,17,5,17c-1.66,0-3,1.34-3,3s1.34,3,3,3 c1.64,0,2.96-1.31,2.99-2.95c2.68-1.33,4.6-3.95,4.94-7.05H18V16z"/></g></svg>"""
svg_pivot = f""" <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><path d="M0,0h24v24H0V0z" fill="none"/></g><g><path d="M21,5c0-1.1-0.9-2-2-2h-9v5h11V5z M3,19c0,1.1,0.9,2,2,2h3V10H3V19z M3,5v3h5V3H5C3.9,3,3,3.9,3,5z M18,8.99L14,13 l1.41,1.41l1.59-1.6V15c0,1.1-0.9,2-2,2h-2.17l1.59-1.59L13,14l-4,4l4,4l1.41-1.41L12.83,19H15c2.21,0,4-1.79,4-4v-2.18l1.59,1.6 L22,13L18,8.99z"/></g></svg>"""
svg_tune = f""" <svg xmlns="http://www.w3.org/2000/svg" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M5 2c0-.55-.45-1-1-1s-1 .45-1 1v4H1v10c0 1.3.84 2.4 2 2.82V23h2v-4.18C6.16 18.4 7 17.3 7 16V6H5V2zM4 17c-.55 0-1-.45-1-1v-2h2v2c0 .55-.45 1-1 1zm-1-5V8h2v4H3zM13 2c0-.55-.45-1-1-1s-1 .45-1 1v4H9v10c0 1.3.84 2.4 2 2.82V23h2v-4.18c1.16-.42 2-1.52 2-2.82V6h-2V2zm-1 15c-.55 0-1-.45-1-1v-2h2v2c0 .55-.45 1-1 1zm-1-5V8h2v4h-2zm10-6V2c0-.55-.45-1-1-1s-1 .45-1 1v4h-2v10c0 1.3.84 2.4 2 2.82V23h2v-4.18c1.16-.42 2-1.52 2-2.82V6h-2zm-1 11c-.55 0-1-.45-1-1v-2h2v2c0 .55-.45 1-1 1zm-1-5V8h2v4h-2z"/></svg>"""

col = pn.Column(pn.pane.SVG(svg_vsc, margin=(0,0,25,0)),
            pn.pane.SVG(svg_ar),pn.pane.SVG(svg_table), pn.pane.SVG(svg_triangle),
            pn.pane.SVG(svg_dev),pn.pane.SVG(svg_drive_file), pn.pane.SVG(svg_settings), 
            pn.Spacer(height=175), 
            pn.pane.SVG(svg_logout), pn.Spacer(sizing_mode='stretch_height'), 
            css_classes = ['icon_bar'],  margin=0,
            sizing_mode='stretch_height')

rb = pn.pane.HTML(""" 
<div class="w3-sidebar w3-bar-block w3-card w3-animate-right" style="display:none;right:0;" id="rightMenu">
  <button onclick="closeRightMenu()" class="w3-bar-item w3-button w3-large">Close &times;</button>
  <a href="#" class="w3-bar-item w3-button">Link 1</a>
  <a href="#" class="w3-bar-item w3-button">Link 2</a>
  <a href="#" class="w3-bar-item w3-button">Link 3</a>
</div>

<div class="w3-teal">
    <button class="w3-button w3-teal w3-xlarge w3-right" onclick="openRightMenu()">&#9776;</button>
  <div class="w3-container">
    <h1>My Page</h1>
  </div>
</div>

<script>
function openRightMenu() {
  document.getElementById("rightMenu").style.display = "block";
}

function closeRightMenu() {
  document.getElementById("rightMenu").style.display = "none";
}
</script>

""")



df = pd.DataFrame({
    'int': [1, 2, 3],
    'float': [3.14, 6.28, 9.42],
    'str': ['A', 'B', 'C'],
    'bool': [True, False, True],
    'date': [date(2019, 1, 1), date(2020, 1, 1),date(2020, 1, 10)]
}, index=[1, 2, 3])

df_widget = pn.widgets.Tabulator(df)


tm = (19,9,0,0)
header = pn.Row( pn.Spacer(width=30), pn.pane.HTML('<h1>App Title</h1>'),  pn.Spacer(width=100), text_field,
                pn.Spacer(sizing_mode='stretch_width'),
                pn.pane.SVG(svg_subject,margin=tm),
            pn.pane.SVG(svg_notif,margin=tm), pn.pane.SVG(svg_tune,margin=tm), 
            pn.pane.SVG(svg_mediation,margin=tm), pn.pane.SVG(svg_pivot,margin=tm),
            pn.layout.DragMenu(df_widget,icon=pn.pane.SVG(svg_subject, margin=(10,0,0,0)), background_color='white'),            
            sizing_mode='stretch_width')

sub_header = pn.Row(pn.widgets.Checkbox(name='Checkbox', css_classes=['cb_custom']), 
                    pn.Spacer(sizing_mode='stretch_width'),
                    pn.pane.SVG(svg_subject, margin=(-6,0,0,0)),
                    sizing_mode='stretch_width', height=25 
)

gspec = pn.GridSpec(sizing_mode='stretch_both')

import holoviews as hv

gspec[4, :3] = pn.WidgetBox(linu)
gspec[:2, 0] = pn.WidgetBox(p21, margin=5)
gspec[:4, 1:3] = pn.WidgetBox(p)
gspec[2:4, 0] = pn.WidgetBox(p123)
# gspec[3:5, 1] = 'https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png'
# gspec[4:5, 2] = pn.Column(
#     pn.widgets.FloatSlider(),
#     pn.widgets.ColorPicker(),
#     pn.widgets.Toggle(name='Toggle Me!'))



col2 = pn.Column(header, 
            pn.Spacer(sizing_mode='stretch_width', height=5, css_classes = ['header_bar']),
            sub_header,  gspec,
            sizing_mode='stretch_width')

pn.Row(col,col2, margin=0, sizing_mode='stretch_both').servable()
