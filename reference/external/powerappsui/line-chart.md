# Line Chart

Source: https://www.powerappsui.com/components/line-chart

## YAML

```yaml
ComponentDefinitions:
  cmpLineChart:
    DefinitionType: CanvasComponent
    AccessAppScope: true
    CustomProperties:
      Animate:
        PropertyKind: Input
        DisplayName: Animate
        Description: Enable draw animation
        DataType: Boolean
        Default: =true
      AnimationDuration:
        PropertyKind: Input
        DisplayName: AnimationDuration
        DataType: Number
        Default: =1.2
      AreaFill:
        PropertyKind: Input
        DisplayName: AreaFill
        Description: Show the gradient area fill beneath the line
        DataType: Boolean
        Default: =true
      ChartData:
        PropertyKind: Input
        DisplayName: ChartData
        Description: Table with x, y, and label columns
        DataType: Table
        Default: |-
          =Table(
              {x: 1, y: 142000, label: "Jan"},
              {x: 2, y: 118000, label: "Feb"},
              {x: 3, y: 165000, label: "Mar"},
              {x: 4, y: 134000, label: "Apr"},
              {x: 5, y: 152000, label: "May"},
              {x: 6, y: 189000, label: "Jun"},
              {x: 7, y: 97000, label: "Jul"},
              {x: 8, y: 128000, label: "Aug"},
              {x: 9, y: 215000, label: "Sep"},
              {x: 10, y: 178000, label: "Oct"},
              {x: 11, y: 145000, label: "Nov"},
              {x: 12, y: 198000, label: "Dec"}
          )
      ChartTitle:
        PropertyKind: Input
        DisplayName: ChartTitle
        DataType: Text
        Default: ="Monthly Spend"
      LineColor:
        PropertyKind: Input
        DisplayName: LineColor
        Description: Color of the line
        DataType: Text
        Default: ="#3B82F6"
      LineWidth:
        PropertyKind: Input
        DisplayName: LineWidth
        Description: Thickness of the line in pixels
        DataType: Number
        Default: =2
      ShowGrid:
        PropertyKind: Input
        DisplayName: ShowGrid
        Description: Show horizontal grid lines
        DataType: Boolean
        Default: =true
      ShowPointLabels:
        PropertyKind: Input
        DisplayName: ShowPointLabels
        Description: Show value labels at each point
        DataType: Boolean
        Default: =false
      ShowPoints:
        PropertyKind: Input
        DisplayName: ShowPoints
        Description: Show circle markers at each data point
        DataType: Boolean
        Default: =false
      ShowTitle:
        PropertyKind: Input
        DisplayName: ShowTitle
        Description: Show or hide the chart title
        DataType: Boolean
        Default: =true
      Smooth:
        PropertyKind: Input
        DisplayName: Smooth
        Description: Use a smooth curve (true) or straight line segments (false)
        DataType: Boolean
        Default: =true
      Theme:
        PropertyKind: Input
        DisplayName: Theme
        Description: Light or Dark theme
        DataType: Text
        Default: ="Light"
      ValuePrefix:
        PropertyKind: Input
        DisplayName: ValuePrefix
        Description: Text shown before each value on the Y-axis and point labels (e.g. "$")
        DataType: Text
        Default: ="$"
      ValueSuffix:
        PropertyKind: Input
        DisplayName: ValueSuffix
        Description: Text shown after each value (e.g. "%", " users")
        DataType: Text
        Default: =""
    Properties:
      Fill: =Color.Transparent
      Height: =400
      Width: =App.Width
    Children:
      - imgLineChart:
          Control: Image@2.2.3
          Properties:
            Height: =Parent.Height
            Image: |-
              ="data:image/svg+xml," & EncodeUrl(
                  With(
                      {
                          Data: cmpLineChart.ChartData,
                          vbW: 700,
                          vbH: 320,
                          Pad: 50,
                          isDark: cmpLineChart.Theme = "Dark",
                          LineColor: cmpLineChart.LineColor,
                          LineWidth: cmpLineChart.LineWidth,
                          ShowGrid: cmpLineChart.ShowGrid,
                          ShowPointLabels: cmpLineChart.ShowPointLabels,
                          ShowPoints: cmpLineChart.ShowPoints,
                          ShowTitle: cmpLineChart.ShowTitle,
                          Smooth: cmpLineChart.Smooth,
                          AreaFill: cmpLineChart.AreaFill,
                          TitleText: cmpLineChart.ChartTitle,
                          ValuePrefix: cmpLineChart.ValuePrefix,
                          ValueSuffix: cmpLineChart.ValueSuffix,
                          Animate: cmpLineChart.Animate,
                          AnimDur: cmpLineChart.AnimationDuration,
                          fnt: "-apple-system,system-ui,Segoe UI,sans-serif",
                          yTicks: 5
                      },
                      With(
                          {
                              BgColor: If(isDark, "#1F2937", "#FFFFFF"),
                              GridColor: If(isDark, "#374151", "#E5E7EB"),
                              AxisColor: If(isDark, "#4B5563", "#CBD5E1"),
                              LblColor: If(isDark, "#9CA3AF", "#64748B"),
                              TitleColor: If(isDark, "#F9FAFB", "#0F172A"),
                              EmptyColor: If(isDark, "#6B7280", "#9CA3AF"),
                              pw: vbW - 2 * Pad,
                              ph: vbH - 2 * Pad,
                              baseY: vbH - Pad,
                              data: SortByColumns(Data, "x", SortOrder.Ascending)
                          },
                          With(
                              {
                                  n: CountRows(data),
                                  xmin: Min(data, x),
                                  xmax: Max(data, x),
                                  rawMax: Max(data, y),
                                  ymin: 0
                              },
                              If(
                                  n < 1,
                                  "<svg xmlns='http://www.w3.org/2000/svg' width='100%' height='100%' viewBox='0 0 " & vbW & " " & vbH & "'>
                                      <rect width='100%' height='100%' fill='" & BgColor & "'/>
                                      <text x='50%' y='50%' text-anchor='middle' dominant-baseline='middle' fill='" & EmptyColor & "' font-family='" & fnt & "' font-size='14'>No data</text>
                                  </svg>",
                                  With(
                                      {
                                          mag: Power(10, Max(0, RoundDown(Log(Max(1, rawMax), 10), 0) - 1)),
                                          ymax: RoundUp(rawMax * 1.15 / Power(10, Max(0, RoundDown(Log(Max(1, rawMax), 10), 0) - 1)), 0) * Power(10, Max(0, RoundDown(Log(Max(1, rawMax), 10), 0) - 1))
                                      },
                                      With(
                                          {
                                              pts: ForAll(
                                                  Sequence(n),
                                                  With(
                                                      {r: Last(FirstN(data, Value))},
                                                      {
                                                          i: Value,
                                                          px: Pad + If(xmax = xmin, 0, (r.x - xmin) * pw / (xmax - xmin)),
                                                          py: baseY - If(ymax = 0, 0, r.y / ymax * ph),
                                                          label: r.label,
                                                          yv: r.y
                                                      }
                                                  )
                                              )
                                          },
                                          With(
                                              {
                                                  segs: ForAll(
                                                      Sequence(Max(0, n - 1)),
                                                      With(
                                                          {
                                                              p: LookUp(pts, i = Value),
                                                              q: LookUp(pts, i = Value + 1)
                                                          },
                                                          {
                                                              seg: Value,
                                                              x1: p.px, y1: p.py,
                                                              x2: q.px, y2: q.py,
                                                              dx3: (q.px - p.px) / 3
                                                          }
                                                      )
                                                  )
                                              },
                                              With(
                                                  {
                                                      dLinear: "M " & First(pts).px & " " & First(pts).py &
                                                          Concat(Filter(pts, i > 1), " L " & px & " " & py),
                                                      dSmooth: If(
                                                          n <= 2,
                                                          "M " & First(pts).px & " " & First(pts).py &
                                                          Concat(Filter(pts, i > 1), " L " & px & " " & py),
                                                          "M " & First(pts).px & " " & First(pts).py &
                                                          Concat(
                                                              segs,
                                                              " C " & (x1 + dx3) & " " & y1 & " " & (x2 - dx3) & " " & y2 & " " & x2 & " " & y2
                                                          )
                                                      ),
                                                      dClose: " L " & Last(pts).px & " " & baseY & " L " & First(pts).px & " " & baseY & " Z"
                                                  },
                                                  "<svg xmlns='http://www.w3.org/2000/svg' width='100%' height='100%' viewBox='0 0 " & vbW & " " & vbH & "' style='background:" & BgColor & "'>" &
                                                  If(
                                                      Animate,
                                                      "<style>
                                                          @keyframes draw { from { stroke-dashoffset: 1; } to { stroke-dashoffset: 0; } }
                                                          @keyframes fade { from { opacity: 0; } to { opacity: 1; } }
                                                          .line { stroke-dasharray: 1; stroke-dashoffset: 0; animation: draw " & Text(AnimDur, "[$-en-US]0.00") & "s ease both; }
                                                          .area { opacity: 1; animation: fade " & Text(AnimDur * 0.5, "[$-en-US]0.00") & "s ease both " & Text(AnimDur * 0.3, "[$-en-US]0.00") & "s; }
                                                          .lbl { opacity: 1; animation: fade 0.3s ease both; }
                                                      </style>",
                                                      ""
                                                  ) &
                                                  "<defs>
                                                      <linearGradient id='aG' x1='0' y1='0' x2='0' y2='1'>
                                                          <stop offset='0%' stop-color='" & LineColor & "' stop-opacity='0.12'/>
                                                          <stop offset='100%' stop-color='" & LineColor & "' stop-opacity='0'/>
                                                      </linearGradient>
                                                  </defs>" &
                                                  If(
                                                      ShowTitle && !IsBlank(TitleText),
                                                      "<text x='" & Pad & "' y='25' fill='" & TitleColor & "' font-family='" & fnt & "' font-size='16' font-weight='600'>" & TitleText & "</text>",
                                                      ""
                                                  ) &
                                                  If(
                                                      ShowGrid,
                                                      Concat(
                                                          Sequence(yTicks - 1),
                                                          With(
                                                              {gy: Pad + ph - (Value * ph / yTicks)},
                                                              "<line x1='" & Pad & "' y1='" & gy & "' x2='" & (Pad + pw) & "' y2='" & gy & "' stroke='" & GridColor & "' stroke-width='1' stroke-dasharray='4 4'/>"
                                                          )
                                                      ),
                                                      ""
                                                  ) &
                                                  "<line x1='" & Pad & "' y1='" & Pad & "' x2='" & Pad & "' y2='" & baseY & "' stroke='" & AxisColor & "' stroke-width='1'/>" &
                                                  "<line x1='" & Pad & "' y1='" & baseY & "' x2='" & (Pad + pw) & "' y2='" & baseY & "' stroke='" & AxisColor & "' stroke-width='1'/>" &
                                                  Concat(
                                                      Sequence(yTicks + 1),
                                                      With(
                                                          {
                                                              gy: Pad + ph - ((Value - 1) * ph / yTicks),
                                                              gv: (Value - 1) * ymax / yTicks
                                                          },
                                                          "<text x='" & (Pad - 8) & "' y='" & gy & "' text-anchor='end' dominant-baseline='central' fill='" & LblColor & "' font-family='" & fnt & "' font-size='11'>" &
                                                          ValuePrefix & If(gv >= 1000, Text(gv / 1000, "[$-en-US]#,##0") & "K", Text(gv, "[$-en-US]#,##0")) & ValueSuffix &
                                                          "</text>"
                                                      )
                                                  ) &
                                                  Concat(
                                                      pts,
                                                      "<text x='" & px & "' y='" & (baseY + 16) & "' text-anchor='middle' dominant-baseline='hanging' fill='" & LblColor & "' font-family='" & fnt & "' font-size='12'>" &
                                                      Coalesce(label, Text(i, "[$-en-US]0")) &
                                                      "</text>"
                                                  ) &
                                                  If(
                                                      AreaFill,
                                                      "<path d='" & If(Smooth, dSmooth, dLinear) & dClose & "' fill='url(#aG)'" & If(Animate, " class='area'", "") & "/>",
                                                      ""
                                                  ) &
                                                  "<path d='" & If(Smooth, dSmooth, dLinear) & "' fill='none' stroke='" & LineColor & "' stroke-width='" & LineWidth & "' stroke-linecap='round' stroke-linejoin='round' pathLength='1'" & If(Animate, " class='line'", "") & "/>" &
                                                  If(
                                                      ShowPoints,
                                                      Concat(
                                                          pts,
                                                          "<circle cx='" & px & "' cy='" & py & "' r='4' fill='" & BgColor & "' stroke='" & LineColor & "' stroke-width='2'" & If(Animate, " class='lbl'", "") & "/>"
                                                      ),
                                                      ""
                                                  ) &
                                                  If(
                                                      ShowPointLabels,
                                                      Concat(
                                                          pts,
                                                          "<text x='" & px & "' y='" & Max(12, py - 10) & "' text-anchor='middle' dominant-baseline='central' fill='" & LblColor & "' font-family='" & fnt & "' font-size='11' font-weight='600'" &
                                                          If(Animate, " class='lbl' style='animation-delay:" & Text(40 * (i - 1), "[$-en-US]0") & "ms;'", "") &
              ">" &
                                                          ValuePrefix & If(yv >= 1000, Text(yv / 1000, "[$-en-US]#,##0") & "K", Text(yv, "[$-en-US]#,##0")) & ValueSuffix &
                                                          "</text>"
                                                      ),
                                                      ""
                                                  ) &
                                                  "</svg>"
                                              )
                                          )
                                      )
                                  )
                              )
                          )
                      )
                  )
              )
            Width: =Parent.Width
```

## Notes

Verified key properties:

- `ChartData` — `{x (number), y (number), label (text)}`, auto-sorted by x ascending.
- `ChartTitle`, `LineColor`, `LineWidth`, `Smooth` (Bezier vs straight segments), `AreaFill`, `ShowPoints`, `ShowGrid`, `ShowPointLabels`, `ShowTitle`, `Theme`, `ValuePrefix`/`ValueSuffix`, `Animate`, `AnimationDuration`.
- No output properties or events — pure visual.

Behavior notes:

- Single Image control rendering `data:image/svg+xml`; fixed 700×320 viewBox with 50px padding.
- Smooth curves use cubic Bézier `C` commands with control points at 1/3 horizontal spacing — avoids the overshoot quadratic curves produce on volatile data.
- Y-axis always starts at 0 and scales to 115% of max — **negative values are not supported**.
- Single series only; for multiple series use a different (area/bar) component.
- No interactive tooltips — inline SVG in an Image control can't capture hover.
