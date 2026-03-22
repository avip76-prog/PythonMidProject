{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e1dca867-7475-4865-a721-58d7d63497b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Amazon File loaded successfully!\n",
      "Rows: 1507, Columns: 17\n",
      "Total Records: 1507\n",
      "Total Records after remove duplicates: 1351\n",
      "  order_date  product_id                                       product_name  \\\n",
      "0   1/1/2025  B002PD61Y4  D-Link DWA-131 300 Mbps Wireless Nano USB Adap...   \n",
      "2   1/1/2025  B002SZEOLG  TP-Link Nano USB WiFi Dongle 150Mbps High Gain...   \n",
      "3   1/1/2025  B003B00484  Duracell Plus AAA Rechargeable Batteries (750 ...   \n",
      "4   1/1/2025  B003L62T7W  Logitech B100 Wired USB Mouse, 3 yr Warranty, ...   \n",
      "5   1/1/2025  B004IO5BMQ  Logitech M235 Wireless Mouse, 1000 DPI Optical...   \n",
      "\n",
      "                                            category  discounted_price  \\\n",
      "0  Computers&Accessories|NetworkingDevices|Networ...             507.0   \n",
      "2  Computers&Accessories|NetworkingDevices|Networ...             749.0   \n",
      "3  Electronics|GeneralPurposeBatteries&BatteryCha...             399.0   \n",
      "4  Computers&Accessories|Accessories&Peripherals|...             279.0   \n",
      "5  Computers&Accessories|Accessories&Peripherals|...             699.0   \n",
      "\n",
      "   actual_price  discount_percentage  rating  rating_count  \\\n",
      "0        1208.0                 0.58     4.1        8131.0   \n",
      "2        1339.0                 0.44     4.2      179692.0   \n",
      "3         499.0                 0.20     4.3       27201.0   \n",
      "4         375.0                 0.26     4.3       31534.0   \n",
      "5         995.0                 0.30     4.5       54405.0   \n",
      "\n",
      "                                       about_product  \\\n",
      "0  Connects your computer to a high-speed wireles...   \n",
      "2  150 Mbps Wi-Fi —— Exceptional wireless speed u...   \n",
      "3  Duracell Rechargeable AAA 750mAh batteries sta...   \n",
      "4  A comfortable, ambidextrous shape feels good i...   \n",
      "5  You can surf the Web with more comfort and eas...   \n",
      "\n",
      "                                             user_id  \\\n",
      "0  AGA2PZGWMQIRA46VYOTICFE7KCBA,AHI2QJ4CLTCQWACDI...   \n",
      "2  AGV3IEFANZCKECFGUM42MRH5FNOA,AEBO7NWCNXKT4AESA...   \n",
      "3  AG2ICOYPSOV5SGBKFEYHGKCNK7PA,AGJ3OQ4X262D3MAQZ...   \n",
      "4  AE6DY6YWTSSE3XNHDXZDGQM2JL2Q,AES3UPSNCD37JZLHZ...   \n",
      "5  AGIOL4B6EPMZ63RZQFWZWI33O2EA,AG33OJYQIXPPS7CON...   \n",
      "\n",
      "                                           user_name  \\\n",
      "0  nilesh,EAGLE,Manoj KNS,Titus P.,Paras singla,a...   \n",
      "2  Azhar JuMan,Anirudh Sood,Hari Krishnan PS,Akas...   \n",
      "3  T N Sivaji,Akku,V,Meet,MOHAMMED,Niranjan koyri...   \n",
      "4  Uday Joglekar,Simi Singh,Hi,chirag bansal,Swar...   \n",
      "5  Chandrashekar SK,Mohammed Ashfaque,Arif Hussai...   \n",
      "\n",
      "                                           review_id  \\\n",
      "0  R2EJIN3N3L3XKI,R2JMJ8QNG66LV4,R3B46JNPC2T4E7,R...   \n",
      "2  R1LW6NWSVTVZ2H,R3VR5WFKUS15C5,R2F6GC79OYWUKQ,R...   \n",
      "3  R5L3FAFS6JXJF,R1VTQ25LXQX5UD,R6RJYAZUM5240,R1S...   \n",
      "4  R3U9FRV2Q625DO,R3EJZ83W9OHW3D,RSH53O0JL66NL,R3...   \n",
      "5  R28ZB0YUM6FKKB,RNB44LXBJIPTL,RVSWATRY0CJIV,R3I...   \n",
      "\n",
      "                                        review_title  \\\n",
      "0  good tool to use for,Brand is always good,Over...   \n",
      "2  Works on linux for me. Get the model with ante...   \n",
      "3  Works Good,Perfect replacement cell for trimme...   \n",
      "4  Handy Mouse,Good quality mouse,Good one.,Good,...   \n",
      "5  Good silent mouse,Too small to hold!,Reviewing...   \n",
      "\n",
      "                                      review_content  \\\n",
      "0  good quality tool from d linkWiFi signal is go...   \n",
      "2  I use this to connect an old PC to internet. I...   \n",
      "3  Works good,Bought it to replace my Phillips QT...   \n",
      "4  Liked this Product,https://m.media-amazon.com/...   \n",
      "5  It's little small for big hands. But best avai...   \n",
      "\n",
      "                                            img_link  \\\n",
      "0  https://m.media-amazon.com/images/I/31+NwZ8gb1...   \n",
      "2  https://m.media-amazon.com/images/I/31Wb+A3VVd...   \n",
      "3  https://m.media-amazon.com/images/I/418YrbHVLC...   \n",
      "4  https://m.media-amazon.com/images/I/31iFF1Kbkp...   \n",
      "5  https://m.media-amazon.com/images/I/31CtVvtFt+...   \n",
      "\n",
      "                                        product_link          main_category  \n",
      "0  https://www.amazon.in/D-Link-DWA-131-Wireless-...  Computers&Accessories  \n",
      "2  https://www.amazon.in/TP-Link-TL-WN722N-150Mbp...  Computers&Accessories  \n",
      "3  https://www.amazon.in/Duracell-AAA-750mAh-Rech...            Electronics  \n",
      "4  https://www.amazon.in/Logitech-B100-Optical-Mo...  Computers&Accessories  \n",
      "5  https://www.amazon.in/Logitech-M235-Wireless-M...  Computers&Accessories  \n",
      "KPI:\n",
      "Number of products in Computers&Accessories: 375\n",
      "Average Rating for Computers&Accessories: 4.15\n"
     ]
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "marker": {
          "color": "royalblue"
         },
         "name": "כמות מכירות",
         "text": {
          "bdata": "AAAAAACAQEAAAAAAAAA8QAAAAAAAADNAAAAAAAAANEAAAAAAAAAmQAAAAAAAACJAAAAAAAAALkAAAAAAAABgQAAAAAAAAEFAAAAAAAAARUAAAAAAAAAyQAAAAAAAADJA",
          "dtype": "f8"
         },
         "textposition": "outside",
         "type": "bar",
         "x": [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
         ],
         "y": {
          "bdata": "IQAcABMAFAALAAkADwCAACIAKgASABIA",
          "dtype": "i2"
         }
        },
        {
         "line": {
          "color": "orange",
          "width": 3
         },
         "mode": "lines+markers",
         "name": "דירוג ממוצע",
         "type": "scatter",
         "x": [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
         ],
         "y": {
          "bdata": "gjwlyFOCEEBJkiRJkqQQQHHq99wSpxBArkfhehQuEEBKkKcEeUoQQNiCLdiCLRBAZmZmZmZmEECamZmZmZkQQGxsbGxsbBBA9mM/9mM/EUB3d3d3d3cQQEqf9Emf9BBA",
          "dtype": "f8"
         },
         "yaxis": "y2"
        }
       ],
       "layout": {
        "legend": {
         "x": 0.01,
         "y": 0.99
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "white",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#C8D4E3"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "white",
          "polar": {
           "angularaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           },
           "bgcolor": "white",
           "radialaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "yaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "zaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "bgcolor": "white",
           "caxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "ניתוח מכירות ואיכות: Computers & Accessories"
        },
        "xaxis": {
         "title": {
          "text": "חודשי השנה"
         }
        },
        "yaxis": {
         "title": {
          "text": "כמות מוצרים שנמכרו"
         }
        },
        "yaxis2": {
         "overlaying": "y",
         "range": [
          0,
          5
         ],
         "side": "right",
         "title": {
          "text": "דירוג ממוצע (0-5)"
         }
        }
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAyMAAAFoCAYAAABE0yRDAAAQAElEQVR4AeydCYCN1fvHv3fGMvZlGDtFKuQnSos2EkXSIkpFyJZUKEQpRaQFlSwVKX8p0kLRTntRlmRLRMq+L2OY7f9+D+91Z9wxd2bu3Pu+d77Mufe95z3vOc/zOee+9zznOee8Uan6JwIiIAIiIAIiIAIiIAIiIAJhIBAF/RMBEQghARUlAiIgAiIgAiIgAiJgE5AxYpPQuwiIgAiIQOQRkEYiIAIiIAKOJiBjxNHVI+FEQAREQAREQAREwD0EJKkIZJWAjJGsElN6ERABERABERABERABERCBoBCQMZIjjLpYBERABERABERABERABEQguwRkjGSXnK4TAREIPQGVKAIiIAIiIAIiEFEEZIxEVHVKGREQAREQAREIHgHlJAIiIAK5TUDGSG4TVv4iIAIiIAIiIAIiIAIikDmBPJlCxkierHYpLQIiIAIiIAIiIAIiIALhJyBjJPx1kHclkOYiIAIiIAIiIAIiIAJ5moCMkTxd/VJeBEQgLxGQriIgAiIgAiLgNAIyRpxWI5JHBERABERABEQgEghIBxEQgQAIyBgJAJKSiIAIiIAIiIAIiIAIiIAIBJ9A8IyR4MumHEVABERABERABERABERABCKYgIyRCK5cqRbZBKSdCIiACIiACIiACLidgIwRt9eg5BcBERABEQgFAZUhAiIgAiKQCwRkjOQCVGUpAiIgAiIgAiIgAiKQEwK6Nq8QkDGSV2paeoqACIiACIiACIiACIiAwwjIGHFIhUgMERABERABERABERABEchrBGSM5LUal74iIAIkoCACIiACIiACIuAAAjJGHFAJEkEEREAEREAEIpuAtBMBERAB/wRkjPjnolgREAEREAEREAEREAERcCcBF0ktY8RFlSVRRUAEREAEREAEREAERCCSCMgYiaTazLu6SHMREAEREAEREAEREAEXEpAx4sJKk8giIAIiEF4CKl0EREAEREAEgkNAxkhwOCoXERABERABERABEcgdAspVBCKYgIyRCK5cqSYCIiACIiACIiACIiACTibgRGPEybwkmwiIgAiIgAiIgAiIgAiIQJAIyBgJEkhlIwLuJSDJRUAEREAEREAERCA8BGSMhIe7ShUBERABEcirBKS3CIiACIiAl4CMES8KHYiACIiACIiACIiACEQaAenjbAIyRpxdP5JOBERABERABERABERABCKWgIyRiKtaKSQCIiACIiACIiACIiAC7iAgY8Qd9SQpRUAEnEpAcomACIiACIiACGSbgIyRbKPThSIgAiIgAiIgAqEmoPJEQAQii4CMkciqT2kjAiIgAiIgAiIgAiIgAsEikOv5yBjJdcQqQAREQAREQAREQAREQAREwB8BGSP+qCguzxCYPGMe6jTudDJYx5e26oWVazciUv5RF+pEXZ2q0+CRr6WpgwU/Ls22qDt378N1dwww+THfbGcUoRfa7UFsIrSCpZYIiIAIuIyAjBGXVZjEDQ4Bu8P6+vSPMXPSUKxcONUbut7ZCu16DIWTO+/BoRD+XOKPJKBL31FYsmIdFs4ea+qgX4926D34RWTXIPlj7d/Yf+AQKlcoa/JlXYdfU0mQEQHFi4AIiIAI5G0CMkbydv3nSe3ZAR44fJLRfc6bI1DnnDPMsf1yT/uWxkApWjjGjtJ7LhH4+59tWL1uE9re0BhlY0uaUi5pUBvFixbGhk1bzeesvnzxza+oVbMa7r/nFmzesgM0TrKaRySnZ3v/6ePxGDGoWySrKd1EQAT8E1CsCDiOgOONEY5q2lMu0k+n4Wff0VN2MjnKysBjBh4zHcOlrXqlmX5jn2caHsP6x6kLTOs7Ks5zTMPAY1smprUuyfCPsjEvf4E6MR/7YubL/Bl47O/a9OXxeuZjx9vTL+zy7LzsMpinzYBl8Lyd1ldfO3369/TX2NfaefqmZ352fEbX2dczbaDXUgfftDym/szL3zmeTx9+WboaDL4d4PRp2GG77carvdE2a5Zjh/Tl2WmoD4Odju/8zMxsWRnHYMfzHAM/k9uipWuMx4BpGFjPzJ9pGHjMOKbnZzvYrFkO49gmuj70LA4cisfoSTPN1CXmZ59nGvsaxtshfb78TLmYH6+109kM+G7H2e+MY/6nC3FlSqJE8aL4YdEKUA6m3bF7r5G3erUK/JilQPkW/LAUl11UFxfXr4UqFeNA4ySjTKiXLa/97is3ZfL9njDNdXcMAPnbefKYcTxnB9887HS+3JiO1/Ba+7y/slg24+00fKeOrAvmwcBjxvGcHaiXHe9bLuViWp5jGjs931kOy2Oedkifhul882O69HowjYIIiIAIiIAIBErA8cYIR0s/fftZcCoNR0s5hcOeUjNuxINmOoe/H0wCKFwoBlPGDDRTP3hNINNvHuvTwXRiOH2HP9rMxw7l40qjsJWn/Tmz9yaN6puyKTNlpw6Ug6FB3ZpofffgNMaRb372tUzLsHj+RGzbscd0UNlp8E1rH7MDzRFPOz3jm7bt5y2DnTOOGH/53W+GG/VhWnJkR5UdFV6TWWA+lIfXMthcM7qezFgPnIbDzuGN115muPBaMiFrdnD8lWtfy7S8btS4GWk6gv6uySyOnVPWB0fgM0vL82wHrCsaL5SDgcw4lchf2yNLc92JqV+sf8ax41bjjEpe3RlP3Zk/09uBhsODQ17CQz1v86Zle+lw/4gs68428foLA4yngeVRdgZ7VJxls43YbYHnWE+z5i5E+jqhXJy+1uyqC71ysZ2y3smCTHg9A8saPOI1b9uzdUv/zu/3wN7tjXHIPD7+8ifTNnk9806fPrPPPy9ZZZKwbpk3uXEKmG+nnwn4HWLHm3pSX8rMwPb4068rmcTInp4N07Ad2N4W6t64TR8wjucYmAd1920bZEk57LL4/alYLhb00FEWBurPgnmO+TDtlu27MXzsNEabwPJYByMGd/PWQUbfv4zqy2SU7iXQdpCZHumy1UcREAEREAERyJRAVKYpHJyAnRV2UH1HVU8nLqffMD07IOk7J/Z17PyyE8jPL0x814zWHo5PADsFjAtW6Nu9rRkRtjtPmeVLuUY91sPIMePDrzNLbowmpueo8/T3vzDpmUeHts3x6v/NNflQBp6gccHATjo/ZzW0v+lqY8BNm/W54ZWV69lZZmeKHbWM6sTOj51grgXYsWufHWXe2bFm543twUQE8EIuHJXPLCk7iWwHtWpWA/W007Msdpj9GROMZ1uz07Zu3siM0PuLpxzp2wANJRoQZGPncectzcw6iDmf/2hHBeWdbYO6PWYZ4XaG7MSzc00PAzupdjzlYkebuttxfGe7oZF53jlngp8ZqP+Lwx7gYaaBbY+B3ip2zmnU8HpeyM5voCPvrCveC6jPmVXL83JkxI3fIU4Pe+GJXt7pYbyAzAc/cJdpx3a9+7JhGspGBiyPbZ73FMbxHAPzaHJZfdj3GbZrtm8aRmTLNPwu0kC/tnFDfoQ9XY0eHZ5jJNO+P/kp1Ktdgx+NIUpjnOWxfBNpvbBsxvEcy7KizF9G9WVOpnsJpB0w78z0SJetPoqACIiACIhApgRcbYxQO44001CgwcDPmQV2aDObR87OIUcV2Tlip4UdQF7DazPLP9DzRQrHgCOj6zf+F+glyOo17MywA8QOBDsSLIgdRnYc2dnkecbZgZ4XdrDsz4G+s/PEkfWs1INv3pyO48/I8E1jH7NeOI3H/pzb72xX1Mu3k2iXSblDJQ8NJxouWWkvtpwZvbNNsG34042eBV4XCGt+B/n9oCHh234uqn/uKetxmKdvoAy33PO4mVZFg5KdanoI6AHwTRfIsb8OPY0SGic0UnxlI0fG87y/vE9X73Z6uzx/9wXG2W3a/t5+9NkPp2yKwKmA/P7Y9UsPmq/uPMc0LJNGOPNk3vzsG1gHPMc0vvGBHLMOAmkHgegRSHlKE1QCykwEREAEXE/A9cZIVmsgLraUmbKS0eJYjgRztJudIgZ2Dhh47DsamdVyg5k+K0ZDRp0UdqSDKZPb8gq048bOHdP60y+ztuTvmuzG2R3B7F7v7zpbN7ZvTiHzDZwKREPL33Xp4zgyT68PjfeGLXrCzsd3mlL6a+zPNPR5TO8R3+nl4nfN1yCh0U79ef50wR5E8NWH8lAuekFoPPB6GiX8DvE4o2Czyeg842mokRFltXW23xnHNAw0KOjtoffHVzau2+D9hmk4MDDt5cHGg8Zr7Xx8vUJ2eUyfPvD7TFmYJv25zD7buvrKZpfv2w4C0SOzsnReBERABNxNQNLnBoE8Z4zwx5o/2vzx5o8rp0ow8JiA2aHhO6d3cBoTvQgMPGa8kwI7MFxPww5cRnJxBJgj6hx5ZRp7rjs9JPzsxMDOLde+cLpLbsjHkWW2AbuuT1cGuZGfvzS+bcnf+WDG2SP1wczT1o2GBL0S/kKgBjjrzL6eax7sjrfvKL8/2dk+08ezPdsGCb0JnFpofz/Tp7U/c3Sf06J4nS2H/c6pZUxn1zfzoiePcRkFm01G5xlvG6M0NOyyfN992zDL5H3GPm/L9NCT4830K+Znf5/tNMzX1+Nkl8e06QMHVzgti2nSn8vss61rIO0gED0yK0/nRUAEREAERMCXQJ4zRvzNb/cFws4RO5/8gWbngItr2SEY8+os32SuOGYHjdMvOFWLulBo6h/oSDPTR2JgR5mBnVcy8qcj47mYmiPy5JV+mg+vyUkHkNdnJdij1zSkfK9je/X97O+YbZltOv250+mWPu3pPr/70ddmjYWdhh1Wrrti55iM7PiM3ul5on6+522DhHFss3w/XaCRze9pej68hlOxOCXLt77pMfT1ljAdA70m1Od0bOjN4G5nNtfM5LPbEvO3Aw1trpWydbfztM/znYYgjStOE6Qxerry2A5Yx0zDa7MSTqerbz6B6OGbXsciIAIiIAIiEAgB1xkj9GgEopi/NJw2wpFWf+slfNOz88kfaMaxQ8ARQ16X2Sgv02cUsttRyCi/zOLZqeIcfnZ26OVhesZxegpHhdlhZFw4AjuCwSyXi5w5rSTQ+qHuXNxPGbhLFjuCPLYD2wl3SNq+c6/ZCIAda3Zc0+9qxGkt7FCyY2lfmxvv7ARyBJ0dahpRLIPGJY1MGps8zzjWL6f4cFoSP9uBbZltOr1BRQ62bryO19vX8PiBIS+ZHaXsuIzel69aD677sOVgOtsLYa89YZy/YLdN6ud7PeuAbZX1xO8e69jf9XYcDQJ6MP15/KgnvSs0Vmi08BpuRkCevuVSZ3KgPrzGZuNb72wr3Cr58JEjZuE7Byv8yUdduFsX31neuCkfpNmdjGWxPigDjSWmeXDIS2nWlPBa1i/rmfXNYJdHPryGgceUgeeYhnFZCb66Un/KZl/PY992EIge9rV6FwEREAEREIFACDjeGGEHkx1Nzl1mh95fZyMjRflDyg4Br2fgWhBOj+CUEn/XMD07QOnPsePCTiB/qClP+vMZfWYHiuWy02p3KDJKcgs8lgAAEABJREFUG4x4dpQ4D51lcq488/xq1mjvImLOmWen2jYGbPmYNn0HltcGK9hysYNP4yizDqpvueyQcd48dSJ/33M5OWanjVPcaEywbTF/O6RvJzQ2+HBEdgztNJSF02gyaks5kY1TyHxlIje2H07zYcfRzpu7PNHI4HnK1bRtP/TseKPZ2cxOw3dew049R9hZ10zLuuc56sY2wmP7HM/zuGjhQt62w/MZhfRy8Hp6IciM+Wd0HeN5nul4bOvB6/mZ+ra65lKQMzvbbNtsSzznGxjHnb/IiPXqe84+5n2DxgqNFsaRCfPnNXa51JnnqA/fbdl86531wjbDQQqm4Tu34PVNQ/mZJzcGoDwM3LWLMvIcA8vioABloCwsi9v18l7B8wzMgwMn9BKxLAaWx3sY2yjTMPCYcTzHNNkJLD+zdhCIHtkpW9eIQPgIqGQREAEnEHC8McIfWHsONTuP/EH0BcfOoB3PH3X+uDPwmIHH9vW+c7h987CP7fS8hsfp45kP5aEMLNO3k2Cn9X3neV7DwGPfc8yf5djx9mfG8dg3rX3MeJ5n4LEdb7+zQ0EdWR5D+nT2eTLjNSyb6eyQPj3T+AaWyTQMPPY9x7zIhGwYzzIoC8tk4DHL4Ts/M40dyNRfPM8zP+bLa+3A9DxnB5bNc+nj7fOne6ecvNY3+JMlEDnsNMzTt8ysxnN6EzuXvjJRR988ecw6YF3Y6Sg3d7BiXPr0tgx2Wt/z6fPxl4Y6Mf/0dedPDl7POmOZPJ9ZYDqm53V2YHn2daxXxmdUPmXiOV+d7Gvtd7uM9Gn4mXnbgezII/119nm++8rGdHbePOcbfNPZMvqeZ9m83g62nr5pfPOw06XPi7ozzj7Pd17nL57nmJbnmIaf7UC9qb9v+Tz2ldO+lvF28D1v56V3ERABERABETiFQAYRjjdGMpBb0SIgAiIgAiIgAiIgAiIgAi4nIGPE5RUo8R1LQIKJgAiIgAiIgAiIgAhkQkDGSCaAdFoEQkmAU2c4hYbTYUJZrsoSAfcTkAYiIAIiIAJuJCBjxI21JplFQAREQAREQAREIJwEVLYIBImAjJEggVQ2IiACIiACIiACIiACIiACWSMgYyQwXkolAiIgAiIgAiIgAiIgAiIQZAIyRoIMVNmJgAgEg4DyEAEREAEREAERyAsEZIzkhVqWjiIgAiIgAiJwOgI6JwIiIAJhIiBjJEzgVawIiIAIiIAIiIAIiEDeJCCtTxKQMXKShY5EQAREQAREQAREQAREQARCSEDGSAhh592ipLkIiIAIiIAIiIAIiIAInEpAxsipTBQjAiIgAu4mIOlFQAREQAREwCUEZIy4pKIkpgiIgAiIgAiIgDMJSCoREIHsE5Axkn12ulIEREAEREAEREAEREAERCAHBLJhjOSgNF0qAiIgAiIgAiIgAiIgAiIgAicIyBg5AUJvIuBYAhJMBERABERABERABCKUgIyRCK1YqSUCIiACIpA9ArpKBERABEQgdARkjISOtUoSAREQAREQAREQARFIS0Cf8jgBGSN5vAFIfREQAREQAREQAREQAREIFwEZI6Emr/JEQAREQAREQAREQAREQAQMARkjBoNeREAEIpWA9BIBERABERABEXAuARkjzq0bSSYCIiACIiACbiMgeUVABEQgSwRkjGQJlxKLgAiIgAiIgAiIgAiIgFMIuF8OGSPur0NpIAIiIAIiIAIiIAIiIAKuJCBjxJXVlneFluYiIAIiIAIiIAIiIAKRQ0DGSOTUpTQRAREQgWATUH4iIAIiIAIikKsEZIzkKl5lLgIiIAIiIAIiIAKBElA6Ech7BGSM5L06l8YiIAIiIAIiIAIiIAIi4AgCYTVGHEFAQoiACIiACIiACIiACIiACISFgIyRsGBXoSIQFgIqVAREQAREQAREQAQcRUDGiKOqQ8KIgAiIgAhEDgFpIgIiIAIikBkBGSOZEdJ5ERABERABERABERAB5xOQhK4kIGPEldUmoUVABERABERABERABETA/QRkjLi3DiW5CIiACIiACIiACIiACLiagIwRV1efhBcBEQgdAZUkAiIgAiIgAiIQbAIyRoJNVPmJgAiIgAiIgAjknIByEAERyBMEZIzkiWqWkiIgAiIgAiIgAiIgAiKQMYFwnZExEi7yKlcEREAEREAEREAEREAE8jgBGSN5vAHkXfWluQiIgAiIgAiIgAiIQLgJyBgJdw2ofBEQARHICwSkowiIgAiIgAj4ISBjxA8URYmACIiACIiACIiAmwlIdhFwCwEZI26pKckpAiIgAiIgAiIgAiIgAhFGIEKMkQirFakjAiIgAiIgAiIgAiIgAnmAgIyRPFDJUlEEgk5AGYqACIiACIiACIhAEAjIGAkCRGUhAiIgAiIgArlJQHmLgAg4n8DkGfNQp3GnNGHwyNecL3iYJZQxEuYKUPEiIAIiIAIiIAIiIAKOIpBtYS6uXwuL50/EyoVTTRgxqFu288orF8oYySs1LT1FQAREQAREQAREQAREwGEEZIw4rELCIo4KFQEREAEREAEREAERyDGBX5auRsMWPc1ULU3RCgynjJHAOCmVCIiACASNgDISAREQARGIPAL3tG9ppmZxitbC2WOxZMU6cB1J5GkaXI1kjASXZ1hzO3QkCQnHksMqQzALPxCfiGOJKcHMMqx5HYhPQlJyalhlCGbh+w4lIiU1cvTZc+CopU8wCYU4r0MbgbnnAm97Tg1/PB1iYYJf3O4Dx4KfaZhy5Ndm78HI0Sc5JRUO1ydLNZ1k6XPgcGKWrnFy4mNJqWD/wMkyZkU29nPcoE/Z2JJoe0NjrN/4X1bUy5NpZYxEULUfS0zF2k2J+G1NQkSENX8n4fe/joVfl9UWzyCE1X8nYtna4OT1WxDkyWkeazcmYsmao8h2Pg5rp3/+k4wlrB+HyZX59/kI/vnuJaR8XBc4uNbvHW3N0SuyX0+ZtLWfVxzJtbx929afm5JCUo5vmbl2bLWxtRsz0cdKk3ndW/cTB6RbuvYoTP04QJbTMsukLdv1vczSh/dr+7Pb35f/mYBVG6y+QYD6Z0nfMNT5Guu3J9EysPze7BTpEAJZE0PGSNZ4OTp16eL5Ua9mDC44NzLCRXUK4cJaua9L/5d24LThZet8EMKgV3ZiwLid6B+EvJyQx6DxuzAgJ7pkxj3E5wdTnxCXedp2F4Asz0/6DdELrkbVzQ8iKuWQuT8lp0Rj19HySEguhPWHa+H5daPQa/IZudbuBk8ITZt+dMKuXNMh1N8nfm8GZ6ZPAPWf0/YTrOupD+8Hwcov1/IJ8H7l1SfA9KFuP1ktb6D1u/OI9fuT1esCSh+Gdjrx/X1ISjK3O0e9xB9JwIuvzwbfKdjO3fswa+5CNLvqQn5UOA0BGSOngaNTIhAIAaURgXAQaF1+GqY0uBbnl/jZW/zm+OrosfxjtFv8C1r+tAbdln6Kedtv957XgQiIgAiIQO4QKFwoBtt37vEuXm/cpo+ZptWkUf3cKTCCcpUxEkGVKVVEQAQin0Bsge0YWftu9DnrMRSKPmwUTkmNxjube6Lr0vnYcLi2iYvgF6kmAiIgAo4kwGeKrDzxfBG+c0G7IwV1mFAyRhxWIRJHBERABDIi0DxuNt6ofw0uLr3Qm4TekN7LZ+PVTYOQmBrjjdeBCIiACASHgHIRgdwlIGMkd/kqdxEQARHIMQHbG/LI2f1QNP8Bk1+KjzdkzSFNAzBQ9CICIiACIuA6AjJG0lWZPoqACIiAkwhcGTsPbzRI6w3ZllAZ8oY4qZYkiwiIgAiIQHYJyBjJLjldJwIiEAwCyiMDAiXy7cYT5/bE0Fr3omi+496Q1FQPPtzaEV2WfAF5QzIAp2gREAEREAFXEZAx4qrqkrAiIAJ5gYDxhlxwDa4qM9+rLr0h/f6YgZfWD0NCSmFvvA5EIGsElFoEREAEnEVAxoiz6gMr/z6Ktz/bH1B45/P92PDfMYdpIHFEQASyS8DXG1Iy/x6Tja83ZPn+S02cXkRABERABFxCQGJmSkDGSKaIQptg34EUvP7R/oDC1E8O4HBCamgFVGkiIAK5QuCiUgvwRjpvyK6jcZA3JFdwK1MREAEREAGHEJAx4pCKiBAxXKlGjUr5oSAG4WoD51WOx7B6A/FMnU6wvSH8Iv1w8HY8tfUbHCp6paPb5xkV8zlavnDVq8rVPUVtIHfaQOW4fLxFKkQQgagI0kWqiEC2CAzuXAahCP3uLIWBHWNDUlYo9Ol7Ryk8cnfk6NOnvaVPp9C0Bbt+hrX+FaPPvhqXFXvH23aTClTAtrpzUPGGt9C3U41M2kvG8j5o6WOXk5vvj3Yqm20ZsyJXqPTJikzZTfuI1c7Y3rJ7vdOu432A9wOnyZVdeQZa97V+1v0tu9c77boB1u/OQ9bvj9Pkyq48tzUrjkIxHu89UwfuJyBjxP11mC0Ndu7eh+vuGIA6jTulCQt+XGryiz+SgC59R4GfB498zZuGcTzHRHznZ6bxzY9xPMc0k2fMAwPT2GXxmOfSh5VrN+LSVr28ZTE9PzOeaXmdnTfzZGAc0zHw2E7HzwxMw7jThTMr5kcoQsWy0ahWIV9IygqFPhXKROGMELELjT6e0NVN3DGc+U8PlF/RGvmObT3ZPKt3Rr7Wq1C+7g05lqV8bGj0qVE5NN+fUOkTirbGMiqUCU39sKzcDrwP8H6Q2+WEKv9qFfKjYtko/99BF97zqpbPh0px0RGjT5Vy0SfvmTqKCAIyRiKiGrOuRNnYkvj07Wdx47WXYdyIB7Fy4VTMnDQUz7z8NuzOv53riEHdzHmm6dC2OXoPfhG2sWGnsfNjmssuqutN07p5I/ywaAXGT/0IC2ePNWXwmMaLfa39XuecM/DVrNFoekUDk455jRjcDQ89OR7p058u3yaN6ht5F8+faMoOxCCxZcjN9+goDzye3CwhtHnni44gZSx0IdNn+0LgkzrAhjesUk/8FSwDNJ4HXDIFKFDyRGTO3vJF2N09ZPWTM+wBXy19AkYV8oS8s/F+HfKCc6nASPrdySVEyjbMBE73cxVm0VR8qAnQGLjgf2djx+69GRZ9cf1aKFq0EP7+Z1uGadrfdLU3DY2U8nGlcV2Ti8DjM6uWR4VypbFj174Mr/c9wfLOrlH5lPTMK7N8CxeKwUM9b8PyVX+dYjz5lvHQizsQivDEq3swcNyukJQVCn2GvrYXA17eGTH6PPn6PvR/KffawqAX/8YPk+9B6ldXA4c3eZvg8qOt8Ph/3+ChWRcEleXQ1/YFNb9QtKnTlTFscuTow3b2pNXeTqevm87xPsD7gZtkPp2sA8ftxBPW/e10adx0buyMvdh3UJvdeG+6OnAcARkjPlXC6Uj+RtEZV+fEdCZ7mpDPZXnu8NChI6DBws7+lDEDQU+ELwTGFy1cyKRhfNEihXBJg9o8DGoIJN+4MiVBeQ/HJ2RY9tK1CXBGkByRWg8p2xbgwWJX4rJCU9ZrMWkAABAASURBVODB8U7BvsTSGLp6AvoufgXfryka9Db4+19Hg55npNaP9NK9J5LbwJqNxzL8/dMJEXACARkjVi3YxsZHn/1gfUr7x3UIs+YuNFOMOG2Io/HDx05Lm0if0hDgFK5D8UcQF1vKeCQOHbaOLaMgTaIcfjBlBJAvPTD05BQpHJPDEnW5CGSdQH5PAh6oMQSjz2uP8jH/ejP4ZlcLdP7tS3y7u6U3TgdhIKAiRUAEREAEwk5AxohVBfe0b2nWGHD9hPUxzd8X3/yKtjc0NlOMeKLZVRdiyYp1p6xh4DmF4wRmfPi18UZwShanc9EwCbYxEEi+NFhemPgu6tU+C/TWHJdOryIQGgLnFl2K1+u3wE0V3oLHc9wbciipOOgNeXLNROxPig2NICpFBERABBxCQGKIgD8CMkb8UTkRx87sth17Tnw6/sbR/tTUVHDE/XiMO1/p8eHUswU/LDUejJxqwQXm9u5cXLDORfE0ADidi1O2OE2K5xu26InFS9f4LY4eKp7/c/2/4PQqv4lORJ4uX1s35sXF9DQ2T1ymNxHIdQL0hnSvNhLj6rVBlcIbvOX9sqcxOi+RN8QLRAciIAIiIAIiYBGQMWJByOyverUKmSXxcz57UfnyAeVKRwcU4kpFIbsbGjU5sePUTx+PBxeu29Jy5yyeoyGR0XoQf/FcUM7duTiVjed5PfNkXszT93z6MpmOgUYDr2c+TM845vPSsAeMjMzLzpvHGeXLc8yHgXkyHwURCAUB2xtye5WJiPIkmyIPJRbHM3+OxqBVb2L3sXImTi8iIAIiIAIiIALHCcgYOc7htK8bNvk8B+C0KXN+8qzKBTCqd1xAYXjPOFQqa1kvOS9WOYiA+wmEUYNoJMKfN2TZ/kvQeemX+HxHmzBKp6JFQAREQAREwLkEZIycpm44Ks8F675JOD3I4/FkOo3I95qsHMeWiEbV8vkDDiWKRWcle6UVAREIMoHqRVZh4vk3wNcbciS5CMb+NRz9Vrwjb0iQeSs75xCQJCIgAiIQDAIyRjKhyAXr3E2LayKYlAvaG9St6V3QzjgFERCBvEeA3pCOVV7ExHqtUaPoai8AekO6LPkMc7Z1sOL4+DTrTX8iIAIiIAIikDMCEXu1jBGrarlwuk7jTuDWvqMnzcSlrXph5dqN4D+uP+BuWo3b9AHTcEH7Y33YyeBZBREQgbxIwPaGdKo2GvmiEg0CX2/I9qNVTJxeREAEREAEREAETk9AxojFh4ucudjZDukXWPuetxdQW5fpLzcJKG8RcCABD1Lgzxuy+uD5kDfEgRUmkURABERABBxPQMaI46tIAuY2gZ63lEQoQvebSqJHiMqSPlmv0+43lThtO+jfeidmNr4Vvt6QZMRgeZHhWFF9AW6+vu5prw9FndzbpiTscPf1xb3Hdtzp3p1+jvXjBBmDVY/UJ1h5OSGfSNKH92ner53ANRgy3Ny4KKKzu/Vmbv8AK38RsAjIGLEg6C9vE2h3TXGEIrS8vBBusX4UQlFWKMpo0SgGt15dLCTsQqHPdY0KoW1TP22haVG0q/QaWuy7HLFJv538ssRehOhWy1DvxkfRrllJhELGzMqg/Ha44crCRh/7s9vfm19yvH7CrUdmdRDIeerA9hZIWjekubVpMbS4rLAjvgPB4HVLk2JoeVlMbusTsvyvvbQoihfxnLx36UgEHEZAxojDKkTiRC6B1NTI0i0l0vSxFDpFpQNrgc8vBZY+DKQkHK/AqBig/vNA85+A4uccj3Pga4qljwPFyrZIKRH0BWI7i6T6YdVEkj5spNSJ75EQ+KBmhkjQRTpEJoHQGCORyU5aRQiB/3YkIRRhz/5UbN2dHJKyQqLPAUufnaFhFwp99h4Atnj1ScT+xc8B884Hdi/ytvTEov/D9ot/xX+xD+K/nSkIhVzZLWPfQThavqzqFUn6sJ2xvWWVgVPTb7W+N3us+4FT5cuqXNt2J+HYMZqM3q++DkQgywQGj3wN190xAPZurFnOIA9dIGMkD1W2VPVPoOeorQhFeOCF7bjv2W0hKSsU+vQZvQP3RpI+Yyx9rLbw+JhF2PPBlSixboDXG5KUkh/T/+uHtt98gK7jiruiDvuO2eEKOQNtq5Gkz71WO+sTQfXD+wDvB4HWpdPTPfHqTuw7JGPE/y+mYgMhQEOEO7QGklZpgLAbIwt+XGq2zOW2uXZgnCrnBIH9fwC/PQgsvB5YOhA4fHzL4RNn9RYEAoePpEIh7zKoVfAbjKx5M2bVOxdvnnchJtZpgrrFfva2rPWHaqHn8jmY/PeDOHAkn9qKvi/+2oDiIqhdHEmQIeK9AeogywT4uAheNG6E1XfjgUKmBMJqjNByHDVuBhbOHouVC6eawGPG8Vym0rstwcG/gO0LAw8b3wHmNwDWvgRsmQesfhaYVx/475PA82B5R/7zS4qMbcOPbsQufUdhzbpNxq2YPp7nmZ5fsvgjCXhgyEvmWSyMoxHp64pkGgbmwXMMPPYnBPNiuUzDvJiGz3hp230o/vl3G+xzvudPl4bpGHgd82ZaBRHIiECJ/LvxxLm9cF7x3xCTLx6lC+5A/qhjJjm9IVM39UPPZXOx4XBtE6cXERABERABJxBwpgzs+/ywaAUe0/PoslRBYTNG2LldsmIdBvZuj7KxJb1C85hxPMc03hMOPYg/mgx/wa+4f74MfNUk8PBDeyDl+APVvPkl7gO+aRV4Hizvn9ney30PapxRCRs2bTVRO3btw8HDRxBbuoSpk2mzPgc783a8SXTipXChGNzc4go88fwbJoaGJB8MOebVWeZz6+aNwC/j+KkfGUNz5qSh4LG/+mRefHbL4vkTcSj+iDFwTCbWSyGrHJ5j/gyU1zZYrNPmL30ajkRcXL8W+M68TSK9iEAGBM4r/iuK5Dt4ytkDiSVAb8hbmx9EMvKfcl4RIiACkU0gxVLP32+7G+OOJqYgKSXVb1/FjfocS7L0SXaWPlZzAQdd2fdR/4M0shaispZcqU8hwC03/IVTEmY/4pQrU0+JyVZE9WoVsH7jf6dc26RRfZSPK41flq7Gjt17UfPMSmkMRl5w3jlnwuPx4M5bmvEjLmlQ2xgTNGBoUPL665pcZK47s2p5VChXGjRsTOIMXg4dOgKWl8Fp0MjZtmOPFoNlBEjxWSIQW2A7OlSxvI5+rpq/vZ28IX64KEoE8goBD39n/f22uzDOg1REkj6WOlYzTAWcVBeWRBzcZb+pYYue4AyN3oNfxOYtO9Dh/hE57rdwMJczRjhzxCoq4v7CZoyww/rp28+CHd/0VBnHc0yT/pzTPheOyQd/wa+cRc8C4hoHHkrU8ZsNSl8QeB4sr3Blv/nExZbyGhBMQIOhSOEYHqJv97bgdDl6SDJyN9JIoaFhLkj3UrRIIWOgpIvO8Ud6b2jU1DnnDMx6dagxdnKcqTLIcwSax83GG/WvwdlF/7B+0E5RH7/uu+rUSMWIgAjkGQLWWJvf33Z/v/dOjyuQP9o89NDpcgYqX4H8UcgXHeWo+oH17572Lc1yA87kYKCHpErFOEx7eXBQ+ioHD8WjXY+hxtChseMbfKfKW6K47i/KdRK7WeBz7geuWRB4aGV1lKrdkVbj2gOBFr8GngfLq3JL2jxOfIorUxL0RhyOTzAeiaKFC8Ge2kRDkNPlLruorjfuxGXmjQYBDQ47vYk88ULvyKHDR8D8T0Sd9o2WftO2/Ywn5rQJdVIEckigRL7dGFn7bjxydj8UzX/A5JaCKOw6Wg4JSYWx8XBNvLLhcfy27wpzTi8iIAKhIKAyREAEMiNQrGhhcNo7DZ30wS0D+BnpGFZjhJ3WLn1HRaSVlxHwLMdfNh24dTdw7SKgndV5Ov+ZLGeR0QX0ghQtWgh//7MN9IA0u+rCNEmbNKqP7Tv3pFnHYSf4eckqlCtb2v6Y5p35cf0H809zws8Huh6HvjAVr78wAP16tPOuYfGTVFEikCMCV8bOwxsXXIOLSy/05rMtoTJ6L38f7RYvQsufV6PL0i8xe8s93vM6EAEREAEREIGII+AwhcJmjNAQ4Xw6jryvXDg1jWuLll8xywJ0GKvwiVOgNBDbEMhXLKgy0KtBb0jnvs+YNSI0Pmgc0N1nu/+mv/8lXpj4rlnM7ls415pwzQkXbDEtXYf0sjAN130wX3pcmBfnTy5euoanTglzPv/RrEnhtCvmx3xPSaQIEcgBAXpDnji3J4bWuhcl8+8xOaWmevDh1o7osuQLrDlU38TpRQREQAREQASCRYB9Krd7LILFIrN8ojJLkFvn2VHl/H8ufM6tMpRvxgRsI4IpaAyOGNSNh2ZeI788jLMDd7Si4cI0nBPJhDzmF40hfTrG8Tynetl5/fTxeNDg4LW+gfkxLePs65jO33oQ5sd4nmd6f4F52PKeOK+3PEzA9oZcVWa+lwK9If3+mIGX1g9DQkphb7wOREAEREAERMCJBALp/zhR7kBlCpsxQrBcAO1v1J2dTXY6mSZQRZQuawTYaacRYRsCWbs6slKXKRENhchiULXUIYyoe+8p3pBPd3dC/7++xn+4XHWea+0+stqS7g15rz5LFQ9b1yiyflyljQgESCCs3zh2hDlNi9N4ONWHgdN6OFUoQPmVTARyTOD5PuUQijDivjJ49oGyISkrFPoMv7cMnnsgznH6jLtrKV6vfw0uKTHP2zaSClTAjgu+QO12r+HpB8/0K7PR58Fyfs+Fgmewyxhm1U+w8wxnfpGkz3NWO2N7CyfPYJbN+0Ak6TOwYxmUKOq9fTj/QBJGPAH2i9k/Zj+ZgeutudwhUhQPmzFigx09aaZZuMxR+oWzxxqujdv0AaEzjYnQiwjkIoGq5fIhFKFsqShUKhuaskKjjweVQ8QuIH0sb0jVv7sjbvkNyHfs+MM8TbOp3hn5Wq9CuXObnraey5QEqjhJnxzKElsCp9U3IKY5lCGYZUSSPmxnbG/B5BPOvHgfKFvKEzHtraJ1ny5YIGzdI3Pb0osI+BLgTCF72jv7y5E2HT1s3zZfsFw3QOi+cYTOz4z3CToUAdcSiPK4VnS/gkc5SaEt84FPagMb3jgpa6EKQGPLO3LJFKCAZWmcPOP3yFH6+JUwa5HRTqqfrInuN3Wk6RNp7c1vpSlSBERABAIgEDZjJADZlEQEQkJg2rz9CEWY/fVhzPjsYEjKCp4+GbP5YMFhTP/0QFj1mfHJFqx/7y5gYUvgyElvyKb8rfFOgZ8xbVmjgOX7cGE8ps/PWN9QMA1mGR9+Ex+w7sEsN7fyiiR92M7Y3nKLVajznfXVQezenxKS+7UKEYG8TMDefIhTtXyD22cTyRjJy61auhsCb3y8H6EIb807gKmfhKaskOkTInb+9Fny3adosv1i1Dg23dQjX/YllsbQ1RPQecHLePUTZKleWT/+ynFr3DSrvblVdn9yR5o+Gba3MH6n/HEPJG7WlweQcIzfQAUREIHcIkBDZNS4GeCShpXpHonh9tkLvuRXAAAQAElEQVREYTNGuB6ElpyvZed7zHNMk1uVqnxFQATcSSAmKh4P1BiC0ee1R/mYf71KfLOrBTr/9iW+3W15SbyxOhABERABERCBjAm44QwXq0+b9TkG9m5vHsHgBpmzImPYjBGuB6Ell966sz/zHNNkRRmlFQERiGwC9Ur8hCkNmuGmCm/B40k1ytrekCfXTMT+pFgTpxcREAEREAERiBQC9rP54mJLRYpKafQImzGSRgp9CBEBFSMC7iSQ35Pg1xvyy57G8oa4s0oltQiIgAiIgAgYAmE3RgaPfA2+07PsY03TMvWTpZcd+xLRY+Q2XN3rH4UsMMgSZCUOOYFziy7F6/VbpPGGHEosjmf+HI1Bq950tjck5LRUoAiIgAiIgAi4i0BYjREaIsRlT83yfdc0LZJREIG8S4DekO7VRmJcvTaoUniDF4Txhiz9Ep/vaOON04EIiIAIkICCCEQiAS5bmPXqUNQ554xIVA9hM0a4GOdQ/BHceUuziAQrpURABLJPwPaG3F5lIqI8ySYjX2/I7mPlTJxeREAEREAEREAEwkYgKAWHzRjhYpyt2/cERQllIgIiEBkEopEIf96QZfsvQWd5QyKjkqWFCIiACIhAlghwd1kuX7CXMqR/5zmmyVKmDkocNmOEDA4eike7HpbbqXGnU9aN2FO4mE5BBBxBQELkKoHqRVZh4vk3wNcbciS5CMb+NRz9VrwDeUNyFb8yFwEREAERcCgBTtPi8gXf5Qy+xzzHNA4VP1OxwmqMFCtaGDMnDYUvUB6PG/EglqxYBzdbeZmSVwIREAFDgN6QjlVexMR6rVGj6GoTxxd6Q7os+QxztnWwPnqsoL+8RkD6ioAIiIAIHCfAhx6m94jYn+UZOc4oy69FCsegWJFC2LF77ynXch9lGiqnnFDEaQmkpgLnVS+IRv8rpCAGrmgDt5y/AW9d2hqdqo1GvqhE076PpRbBnIRn8Z7nI9Q452xX6KHvnO45ebkNXFArBh5YP0DmG6wXFxOQ6A4lwMH5UeNmgIP1HLRnWDh7LC6uXwt8l2ckmxVXuFAMpowZiCaN6p+SA3cL4K4BbnY5naJUCCKKxHjQ/ZbiGN6zbESERzqVwhNdYyNCF9bJI3eXwtAI0mdAh5J4snuZ7NVPj1gMv2wCehdrjgrRq05+O2IvQoEb/0DrLv2tfOOsELq23P+uEniqR+jKY5vIzfCQpU9u5h/qvCNJH7YztrdQM8yt8gZ2jEWlstEnv8c6EgERCDoBDtJzsN7OmH3k8nGl0fruwVi5dqMd7cr3sE7TCiuxCC08NYIGp1JSUhFJ+iRTnwhqd9QnW+ocWAt8fimw4gkg9bg3BFExQP3ngeY/AUXDs3VhtvXJFoTcvyg5OYJuBhauiNPHuh9YakXMX2S1toipFikSIQRoeHCQvk66rX1HDOqGrne2wkNPjnf10gYZIxHSUG01tuxMxqatiRERtu1Kwb87kiJCF9bJ9t0p2Lw9cvTZscfSZ1vg+mzachR7f3kWqfPOB3YvspssjhZriP8aLsamkg9g07bwtd8de1Lxz7bI+O6wve3cmxox351I04ft7PCRFO93QAciIAIikF0C97RvCU3Tyi49XRd0AvFHUzFl7n48OnFnRISnJu/G46/uighdWCeRps+wKXvw2KTA2tqY15cgcf6lKLV+IDwpCabtJ6bE4O0dj6Prr+9j4Fulw17Pw9+w9ImQ7w7b29OWPnyPlBBJ+jz9xi7sPWi+Brn5orxFQAREwBUE5BlxRTUFLuTOvcnYsjNJQQwc0gYScWH0Gxh5RlOcVWiptyGvP1QL9yydh9f/vAf/7UxxiKz63ujeEZo2sG1XElLkGPHeD3QgApFBQFpkl4CMkeyS03UiIAKnJVCu4GaMrns7+pz1GApFHzZpk1LyY+qmfui5bC7+PVLDxOlFBERABERABEQg7xKQMZJ36z5HmutiEciYQCpal5+GKQ2uxfklfvYmozek5/I5eGvzg0hGfm+8DkRABERABERABPIugbAaI/FHEtCl7yjYD23xfXf7A1zybpOS5nmZQGyB7af1hmw4XDsv48mJ7rpWBERABERABCKSQNiMERoivQe/iMsuqgs+vMU3zJw0FNxPOSKJSykRiFACzeNm443616TxhmyOrw55QyK0wqWWCEQ0ASknAlknMHnGvDQD7Pyc9Vzy3hVhM0YOxyfg4OEjuKSBRkrzXrOTxpFEgN6QkbXvxiNn90PR/AeMaimp0Xhnc090XTof8oYYJHoRAREQARGIYAIcZF+/8T/wiegrF04177PmLsSCH09u3hLB6udINWOM5CiHbF7MB7jUPLMSXpj4LliBvtnwoS58uAvT+MbrWAREIPwE6hZbhDF1b8Mnl9bGew0bYvoFV+Di0gu9gtEb0nv5bLy6aRASU2O88ToQAREQAREQgUglULhQDPgQQrvvWqRwDCqWi8WGTVuDojL7ypG6tCFsxghrhpXGaVoNW/T0urW0VoRkFCKcgGvVKxR9CE/W7ol6JX5GoejDKF1wBwpEHzX6pKZ68OHWjsYbsuZQfROnFxEQAREQARHIiwT+/mcbVq/bhOrVKuRYfRoikby0IWzGyM7d+0DDY/SkmejXo51ZN0LXFmuscZs+5hzT8LOTQ/zRZDglJKekOhmVZIsAAmcXWYGS+Xefokl8UhH0+2MGXlo/TN6QU+goIvwEnCcB79ZO+e3IqRxHjiWDPz85zccp1ydY+iRbFeQUeXIqx9HEFCRZFZTTfJxy/bEkSx+rgpwiD+XwvcOw78r+bbseQ9H1zlZo0ijng3ORvrQhyhdgKI/pxvr07WeNEXJP+5amaN84nuNnc8LJL6nWHcspweIUbdWoAiAGwWdQusBudKo62mplp/59s7sV/jh4qbjr+6c2EGAbMN8ip/x25FAOj/Uz6IH1ksN84JDrPVbleBwiSzCYsG5YR8HIK+A8cpWfVUFOa28U6URg35V92MXzJ+KHRSsQjEXszDOSlzZYt80T9PSWLQKFY/LBKaFgtAfdbiqJZ3rHRUR4+t6yGHlfZOjCOnGzPhPv/B4zGjVHvZKL/H5PzrnkBte3ueE9y7heB7YzOwyTPo6tz8e7lUXxwnDMb0dOf8NiCkbD4/FEjD4FC0QjKipy9CmQPxrRVv8gp/XslOsL5I9CPmvE0SnyUA74+cc1JFyKwEXtfk5nOSqSlzZEZZlGkC6w3Vi+zxbxPaaLi2mCVFxuZuOYvAsU8KDWmflxwbkxERHOPTMf/ndWgYjQhXVyzhn5UK+my/SpnoALdt6FGn/fifxJu463dWsAFDHlgXxFgWLnAP8bhuqX3un6eqpZNRr1z4mM7w7b21lVol1fJ9TDDpGkz/lnx6BU8SjonwiIQOQQYJ918MjXvJsy8TN306pxRqUcK8m82C92+9KGjECE7W5YNrYk6Mbi9mf+As8xTUaCK14ERCCXCWyZD3xSG9g8+2RBhSoATeYBt2zFvha7kXz9auC8x06eD8lR7hTiyZ1sw5ZrpOkTNpAqWAREQAQCIGD3WRue2JSJ65/b3tAY9lKEALLIMAnzZr+Y/WU7P984nuPnDDNw+ImwGSMO5+JK8Y4lAqs2JGLRyiMREf74KxFL1h6NCF1YJyvXJ+K3Nc7X57flW7Hz07uBhS2BIye3JNxZuiN+q/4bFu1tbOpk5YYk/LoqwRxTP7eHlX8nY/GqIxGjz+qNyRGjC9vW/sN0ybny1ux+oaWBCIhAQAQ4lYoGgx1swyGgi/NworAZI7bLqU7jTri0VS+sXLsR9j8u9qE7imnsOL1nToC7ZUz6YB8eeWVnRITHJu7C4PGRoQvrxA36vP/2TFRbcj7K7nnL2+B2HY3DIyun4rY5w9B/UqK3bQ2ZtAuDIqh+Hqc+EfLdYXujPnyPhPDohJ3Yuz/F2yZ1IAIiIAKRTMCfbtzeV88Z8UcmB3F0J9GtROtxzpsjMPSFqVi0dA0ImnPicpC1LhUBEcgigZioePSv2R/P1OmEMgV3eK/+ZlcLdF7ypeUNaeKN04EIiIAIiIAIiEDoCNAQ0XNGcpk3DZNenW5E577PgDsPzJw0FMWKFs7lUpW9MwhIinATqFfiJ0xp0Awtys30irIvsTSGrp6AJ9dMxOHkEt54HYiACIiACIiACISWgJ4zksu8OT2L07RGjZsBPvRQ8+tyGbiyF4ETBOgNeaDGEIw+rz3Kx/x7IhYw3pDfvsS3u1t643QQQQSkigiIgAiIgKsIcNBezxnJhSrjehCuC+ETKptcVt/srEXYuVCUshQBEUhHwPaG3FThLXjM07AAX2/I/qTYdFfoowiIgAiIQHYI6BoRCAYBLo7n7KGGJ3br4ppr9qPZnw5G/uHMI2wL2Kk0p2JxShYB87OCCIhA7hLI70mAP2/IL3sao7O8IbkLX7mLgAiIgAiIQDYI0OCg4cE11f16tAPXW3M2EbPiFsI8xzT87MYQZGMkcAT0gsx6dSjqnHPGKRcxjueY5pSTihABEcgWgXOLLsXr9VvgJh9vyKHE4njmz9EYtOpNyBuSLay6SAREQAREQARylQD7w/amT/ZyBt84nuPnXBUiFzMPmzFi67Tgx6Wgqyl9cLuVZ+undxHIVQIBZE5vSPdqIzGuXhtUKbzBe4Xxhiz9Ep/vaOON04EIiIAIiIAIiIAIhJJAWI0RGiL2wnW6nHyD2628UFaiyhKBjAhUL7LKeENurzIRUZ5kk8zXG7L7WDkTpxcREIHACCiVCIiACIhAcAmEzRjhnsnTZn2Ogb3bw82upeBWh3ITgeAQiEYiOlZ5ERPrtU7jDVm2/xJ0ljckOJCViwiIgAiIQG4TUP4WAa4H4Yyh9LOI7M88xzRWUlf+hc0YsfdMjost5UpwThW6RuX8OK96QYU8zKD52X9h6sWt0anaaOSLSjRN9WhqEczc9wymHP4AFSpXVfvIw+3DjfeHOlZ95c/nMW1ZLyIgAiKQ1whw0J4zhnxnEPke8xzTuJVL2IwRtwLLVblzmHnhgh70ub0UXnq4XESEkb1j8UKfshGhC+uE+ozum4v69CuNl66dhEfKXYdK+VedbE1xV6HgjX+gXa+BFsvyVghO+3i6V2mM7RcXtPzIKJxh+L2WPg8Fh0049bDLHmbpYx+7/X1sv3KoUk4/Vye/1DoSARHISwTo9aD3o07jTuCz+fiMPlv/yTPmgeeYxo5z27vu7m6rsUzkTUlNzSSFe04np6QigtRBUnIu6nNgLfDphcCKJ4DU494QRMUA9Z8HrlkAFD1117qctgSjT04zCfP1vsUnJaf4fnT9cWJSZOlj3Q5cXydSQAREQASyQ4BeD3o/6A2Z8+YIDH1hKhYtXYMufUeB2/1mJ08nXRM2Y4RguX0vt/F1EhC3yxLliZypDPmiPIggdZAvOhf0SbU6nKtfAOadD+z7/WTzjb0IaLkMqPWQFeexQvD/jD7BzzZsOebPF7bbYa7oHGV9f3IliGwqYAAAEABJREFUY2UqAtknoCtFQARySID9516dbkTnvs+AD0Hk8/r43L4cZhvWyyPr1zesKMNfePzRVIyZsRf3P789IsLAcbvRb+zOiNCFdfKIpU/fMcHTZ9iYH7DxTcsbsvRhICXBNMDElBh8sP8JPPD7h7j/1ZK5ym7w+D14cPSOXC2D3EIVjD4vRMZ3h8z+/vf47mmmYehFBERABETA9QQ4PYvTtOydaO1njmSsmDvOhM0Y4dw2znHj/DcGupq4w5bTsNkVTxntQLkpv9NkpTwb/kvEyg1HFSKYwaoNR1A74WUMLNMUZxRYymo3YfXB83HP0nl4eUUX/PG32kFe/x4cTUw17UIvIiACIiAC7ibAPif7nu16DEWTy+qDU7boIXG3VielD5sxQoiEyflvDFPGDEThQjEnJXPQUfFiRUA3GOVkoNyU30EiShQAeQFCuYKbMa7ezbi3+tMoEH3UqJyUkh9TN/VD7+Uf4N8jNUycXkRABERABERABCKHAKdisS86YlC3yFHqhCZhM0ZOlK83ERCBgAikonX5aZjS4FrUKrbMe8X6Q7XQc/kcvLX5QaRCX2cvGB2EgoDKEAEREAERCAEBDoBntM6aa695jmlCIEquFBHW3gunZXF6lj39yfed7ii6pXJF6yxmeuDgYdA1RvmcJFcW1VBylxKgN2R03dvR56zHUCj6sNHC9ob0XDYXGw7XNnF6EQEREAERiGQC0k0EIpNAWI2R4WOnGaqL508Epz/ZgW4ouqPMyTC/0OL86ePxXvka1K2JgcMngYZUmEVT8RFP4KQ35PwSP3u19fWGJCO/N14HIiACIiACIiACkUeAg/McDOeguG/gM0YiQduwGSMEu2TFOnRo29zvWhGnwr3zlmY4ePgIDscf373IqXJKLncTiC2wHem9ISmp0Xhnc0/IG+LuupX0IiACIiACIpAVApyCxfXK9qC9/c48aKSwT81jt4awGSMERu9HXGwpHiqIgAicINA8bjbeqH8NfL0hm+Oro/fy2Xh10yDkkjfkROl6EwEREAEREAERcAMBbu07sHd7jHl1lhvEzVDGsBojGUrloBPvfvQ1uL2vLdL0979AzTMrgVaqHad3EQgGAXpDRta+G4+c3Q9F8x8wWdrekK5L52PNofomTi8iIAKRQEA6iIAIiEDgBNgX5TNGfKdp8bj34BfBmUZu9o6EzRgpUjgGxYoU8i4MJ1A7cLH4wUPxgddQLqaMK1sqjYzbduzBY3065GKJyjovErC9IReXXuhV39cbkpjqzG2vvcLqQAREQAREQAScTMDFstHQeOjJ8Thg9Y1vvPYy7zpmTtfiuuuK5WLxx9q/Xath2IwRPlOEzxYhSH+Bc+Oc4H1o0qh+mkqnzJTdtTUuwR1FoES+3UjvDUlN9eDDrR0hb4ijqkrCiIAIiIAIiEBYCLA/zH4x+8vpnzPCPullF9XFF9/8GhbZglFo2IyRYAivPNISiEoFbmpcFPe3KxUR4b62JdG7bamI0OX+dqVw361p9Rl5wzd4p1Ez+HpDDkdXxfdlPkbqBePQs20FR+tu9LH0om6REKhPJOhh61AoxpP2BqFPIiACIiACuUpg8MjXYM/y4Xuodrvi2pH0RkquKhrkzGWMBBloOLOLsTofTS4ohJsbF4uI0OziQmh1eZGI0IV1Qn1uuMLS55IE3BzdGRfv7YiCKbtPNBmr43j2fSjSZhWuuLalK3Ru2jAGN15Z1BWykn9m4eoLC+LGq7L73XHedVXK6fZ+4sulNxEQARHIdQL2Ix8Wzh5rZtTwMRWvT/8YC35cmutlu70A/Vq5vQYlv/MJ7F4MfN0cxT+JRf45FYGPqgGbZ5+Uu4j1uenXwIXjgHxFTsY7/MhyxDlcwqyJF2n6ZE17pRYBlxGQuCLgMAKcLkXvBKdUUbQzq5ZHrZrVsGHTVn5UOA2BqNOc0ymXETh2LBVrNyViyZqEiAhrNiZhxV/HXK3L0lUHcGzBrcC2L4Ckg0DCdiD5iLdl7Y7tiGVn/YYley9xnZ7r/knG8j+Puk7ujL4f2/fIHPE2TB2IgAiIgAjkiACfR7dl+25Ur1YhR/k45eLclEPGSA7pxh9NhlPC0eRUTJy9DwPG7YiIMHj8Tgx8xd26TJz6Awoc++eUVnYspQAGrZqK2+YOw8MTDruyvgZP2OlKuTP6fvy7IwlHHPR9zul9hY0up3kEcv2RYykhuQeGSp9AdM5pGrYzmr45zccp1x85lowUSyGnyJNTORIsfayf05C065zKGsj1RxNTkGRVUCBp3ZDmWJKlj1VBTpKV96f0gc/+aFC3JrgRUvpz+pyWgIyRtDyy/inVugM7JVjSW/cbpKRAIUcMgsOvkGc/OlQZY9XKqX9L9l2GX/Y0UT05oJ7s7wusrzL44pTvc07lYLPLaR4BXW9VYkDpLMA5SRcyfXIoZyA6mnZmKRRIWhek8VjIPEYn68AF8iITGT1W1XgySZNZHk46z7phHTlJppzJYlWQ09obRfIJXMiuR0H4AMnkMGzGCPdMvu6OAWl2HWDlZSKv404XjskHp4ToKI/j+ORVgS4qtQBvNLgGl8d+4RfBj3ua+Y1XZBgJWF+fQgXzOeb7nNP7CknmNI9Arg8KswDuo6HSJxCdc5qGzDweRExbiykYDY/HEzH6FCwQjSjr9zSn9eyU6wvkj0Z0dOTUT4H8UcgXHeWo9gaff+zL0hAZN+JBcB2Jz6kcHXJnLu7Q5S/wXI4yD/PFUeEqnwt87D2TVy6canYeaHbVhcY4oZFCYyVcsqlcEcgugZioePSv2R/P1OmEMgV3HM/GGizceywWR5KKYMuRavi/f3pj3vbbjp/TqwiIgAiIgAiEmICKyx0CNESYczCfScc8aYDMmrsQ9k5ddr+Z74zjOaZhWpbvthA2Y8QfKM6rI1jOseNcO39pFCcCTiVQr8RPmNKgGVqUm+kVcV9iaQxdMwFtFi3B9T+vwl2/fYsp//RHSmo+bxodiIAIiIAIiIAIuJsAB9GXrFiHjz77wQys0zhg6NJ3FOxtf7OiIfPj4Dy9LHzKOgfwOZCfPg/G8RzTMC2v4bXp0zn5s6OMERsUPSSs0ODAtHPVuwjkDgF6Qx6oMQSjz2uP8jH/egv5ZlcLdP7tS3y7u6U3TgciIAIiIAIiIAKRR8A2Cjio7hty4iXp3eVmBHo9p4QxLa9xG92wGSM0NGi90Wpk4DHjCDAuthSKFS3MQwURcDSBc4suNd6Qmyq8BY9ZIQgcSiqOoasn4Mk1E7E/KdbR8ueKcMpUBERABERABEQgRwRo3LS65tIs58FreG2WLwzjBWEzRgiKbiXbemx7Q2PYU7N+XrIKxYoUQpHCMWFEo6JFIGMC+T0J6F5tJMbVa5PGG/LLnsbovETekIzJ6YwIiECwCSg/ERABEXAzgbAZI+mhXdKgNtb9/R84t+716R/joZ63BXUXgvTl6bMIZJcAvSGv12+B26tMRJQn2WRzKLE4nvlzNAatehO7j5UzcXoRAREQAREQARGIOAIhU4gzhtp2H4qVazd6y2QcZxNxVhGD23fSomJhM0bSw2zXYyhW/bkRl11UFz99PB51zjmD8imIgGMI+HpDqhTe4JXLeEOWfonPd7TxxulABERABERABERABIJJgAvhBw6fBM4m4swieyetBT8uDWYxIc8rbMZI+mlahMpwT/uWIYcQSQXGlYpGpbL5gheUl2F5SeW1mNowrTckIaUIpm4fiXE7pyOmRCWTTuzd2/YK5PNE0q1AuoiACIiACEQYgb//2YaDh4+gdfNGRjP2pQf2bo9psz7P1o5dJhMHvITNGHGA7hEnQuGCHnRuVQLDe5aNiPDYPbEY2q1MeHXpXhIvXzsJI868HhUKnPSGJJS8ErsaLUWT2x8KWD7q82T3MOsTxLbxaJfSeKpHZLQ1fmeqlo92xD1BQoiACIiACIiAPwI7du89ZU01N32igXI4PsHfJa6IC6sxQrcS57v5C5wPx6lcrqDoICErxkWjWoX8EREqlIlClXL5wqdLzCpUW34pSm58CkhNPF7L+YoCDccjpuVCVK5eM0uylY+NCq8+QW4X5UpHoWr5MNZPkPUpUVSekeONXK8ikKcISFkREIEwEwibMUJDY9S4GRg34kFwepZvmDlpqLb2zWbD8ERQfyoqyoOw6JNiGR4rLAPk04bAvt9P1kTcVUDLFUDNe604jxWy9mf0ydoljk5tVY+j5ZNwIiACIiACIhBpBLZs3w1fL4j7dqA9tUbCZoxQFD5LhO4lHivknMDRY6mY+91hTJ6zLyLCjE8P4s1PDoRUl/c+XIzdM+sDK56A7Q1JRgx+KTAMk+M/wOSvS2ZbnhmfHcTUEOuTm21h7aaknDda5SACIiACIiACIpAhgYOH4sFNnjiLqPfgF9Ok44L2HxatMJs/8aGHaU666EPYjBEuupn16lC/u2ZxJy2eYxoXsQy7qMmpwBe/xGP6pwciIsz4/CDe/uxASHR5+9N9OPb782h98ArEpqz01uXqg+ej82/zMOjrjpYcB62QNXl86+KdEOrjW25uHW/dJWME+icCIiACIiACuUSA/WDfZ/JxFhE/M55F0gCZMmYg3L75U9iMEUJUEAEnEKhcaD3G1bsZ91Z/GgWijxqRjiUXxIQNj6L38g/w75EaJk4vIiACjicgAUVABEQgoglwmUP6Z4+4XeGwGiN0L3XpOwp0PaUPWsDu9qblfPk9SEHbiq/i9fNboFaxZV6B6Q3pumw+Zm3pjlSE9SvilUkHIiACIiACIuA8ApJIBHJOIGw9LRoinPvGhxzS7eQbtIA95xWrHE5PoFzBzad4Q5JS8mPqpn7yhpwenc6KgAiIgAiIgAiIQNAIhM0Y4U4A3Bf5kga1g6ZMbmek/COBQCpal5+GKQ2uTeMNWX+oFnoun4O3Nj8ob0gkVLN0EAEREAEREAERcAWBsBkjXHxT88xKeGHiu6c8NVIL2F3RdlwnJL0ho+vejj5nPYZC0YeN/LY3pOeyudhwWIaxgeKcF0kiAiIgAiIgAiIQ4QTCZoyQ64hB3cx2ZA1b9PSuG9FaEZJRCC6Bk96Q80v87M3a1xuSjPzeeB2IgAiIQN4kIK1FQAScToCD+dxxlgP3Tpc1UPnCZoxwNwAaHqMnzUS/Hu3Mgw8Xzh5r5G7cpg94jmlMhF5EIJsEYgtsR3pvSEpqNN7Z3BPyhmQTqi4TAREQAREQARHIOQHlYAiEzRihZce9krlw3d4f2TeO5/jZSKkXEcgGgeZxs/FG/Wvg6w3ZHF8dvZfPxqubBkHekGxA1SUiIAIiIAIiIAIhJbBy7UZc2qqXdxaRvQMt43gupMLkQmFhM0ZyQRdl6WwCIZOO3pCRte/GI2f3Q9H8B0y5tjek69L5WHOovonTiwiIgAiIgAiIgAg4mcDkGfPQ9aFn8foLA8wsIg7i24FxPMc0TtYhM9nCbows+HHpKZYe4zITXOdPJSbJ5iYAABAASURBVMDKbNmoMLrcUCIiQqdWxdG5VYks6TL82nmYfnEzXFx6oRfQ/qiz8Fnxz5D0v2fQoVW5LOUXTJZ3X188y/oEs/xg51U+VutsvI3MkQcSSgREQAREwM0E+BiMHxatwIjB3eBvjQjjeI5pmNaturL/GjbZB498DaPGzQDXithWHo8Zx3NhE8ylBccU9OC6S4vgrhYlIiLc0qQIbmtWLDBdmhzDXTG3o9Hhe1Egdf+JGvQAZ9+HEm1XoMUNTQPLJxfZUZ/bmweoTy7KEaz2cc4Z0Sc4600EREAERABCIAJBJmA/BiMutlSGOfMcH5XBtBkmcviJsBkjXJy+ZMU6DOzdHr5rQ3jMOJ5jGofzc5x4qY6TKPsCpQSqzD/vAZ/UBrZ+erKwItWApl8DF44DomNOxofxKGB9wihjVopODbR+spKp0oqACIiACIiACBgCRQrHoFiRQtixe6/57O+F55iGaf2dd0Ncdo0RN+iW52T0WBpv352MzduTIiLs2JOCLTuTMtTlv81bEf9FG+D7tsDRXZb2/PPgUOV78W/D5diMyzO8NhyM9h1MoYAKIiACIiACIiACIpApgcKFYswjMAaPeA3+Fqozjucuu6gumDbTDB2aIGzGCD0g3DGrSaNTFxMzjueYxqHcHCnW4aOpeOW9feg3dntEhEGv7EL/l3f61eWt12eg6ILzUHjn+9662JNYDk9smInO8x9F35cP+b0unGx++SPBK2vWD3SFCIiACIiACIhAXiPAHWfthep1GndKs86ai9d5jmnczCVsxoiboTlZ9v2HUrB7f3LEhoRDe9Alrh8ePbMjSuTb462K+dvb4e5fv8B3Wy5yrO5HE73i6kAERMDpBCSfCIiACDiEABeq//Tx+FN202IczzlEzGyLIWMk2+h0YagJXFRqAd5ocA1alJvpLXrX0Tg8snIqnlv3HA4nl/DG60AEREAEREAERMA9BCJJUm61q42YAq/RsBsjC/xs7Us31HV3DIAWsAdekZGcskj0fvSv2R/P1OmEMgV3eFWlN6Tzki+xaG8Tb5wOREAEREAEREAERCAcBOw+7ehJJwdNwyGH28oMqzHCSuM2vtzO197a136P7DUjbmsmoZX3zMJrMLJ2J8y95Dy8d9GFmNnw4jTekH2JpeUNCW2VqDQREAEREAEREIFMCHDNM/ux/Xq0yyRl5qc5IP/xlz9lnjBdCl7Da9NFO/pj2IwRPpxl2qzPT9na19G0JFxICAw5pzcuLr0ARfIdROkCO1Eo3xFvud/saoHOv8kb4gWig8AIKJUIiIAIiIAIuIzAuCkfoEvfUWCfOTPRmYZpeU1maZ12PmzGCB/Owoe08GEtToOSFXnijybDKSE5Ah5kUarADpxRZN0pVZCUmg9DV0/Ak2smYn9S7Cnn3RJxNCnFMe0lp+02JRU4csw57T+n+ljq4IiDvs851YffiZzmEcj1R46Fpk2HSp9AdM5pGrYztrec5uOU63kf4P3AVx43HydY97Vkq4LcrIOv7EcTU5BkVZBvnJuPj1m/o0lWBTlJB96fgh24oyxnCZWPK42GLXoio+UL9ILwHNMwLa/htcGWJzfzC5sxkptKhTRvPvnNKSGkige/sJioeHSt9qzfjNcerIdvd7f0e85NkR6ntJUgyOFBKjypFv0g5AVH5GHpYunkDFkssDllYtQJQj6ZypGCkDALmT4hYGbamaVQpmxDIEsQZOB9gPeDkLSDIMibmZx8Zpfu1U5ue9Z3x3yHHCQjRcqlMGJQN7OLFh8I3rhNnzRb+3KNNeMG9m5v0jBtLomRq9nKGMkh3sIx+eCUEB3lyaE24bv83KJLMaVBM7QoN8vq2Jwqx6K9jU+NdGFMgfzRjmkvOW23Ho8HMQUjSR+gUMF8EVM//HrktI4DuT5UzEKlTyA65zQNmVlfn4hpa7wPeDyeiNGnYIFoRFm/pzmtZ6dcz9+d6OjIqZ8C+aOQLzrKUe0NIfhnr0dZuXCqMTx833kuBCLkWhFRuZZzJhnThTTr1aGIhP2RM1FVp09DIL8nAd2rjcS4em1QPuZfb0ouUo9PKoJtCVUw899umPlfN+856EgEREAEREAEREAERCAiCITNGLHnuNHF5C9w/hvTRATlECpRqKAHRWLcEerHLsPkC1rg9ioTEeVJNpQOJ5XAmI1j0GH5Mty2bDW6/fEDpm0bgnwFCrtGr4z454s2KupFBFxHQAKLgAiIgAhkToC7xLJPy619P/rsBzOlinGZX5m3U4TNGKFnhItsfN1Mvsc8xzR5u3qypr3lVcad1xXHkHvKODo83rkoXm0xFi/UvgWVYzZ4ldxXrDn+/N8SXHZTDyP/oE6xeLSLs3XJCuvaZxT06qoDERABERABEciAgKJdSoDTpXz7sjxmnEvVCZnYYTNGQqZhHioopoAHdc8qgIvqFHJuqPgnGm68BBV2jgZSj3tDkK8o0HA8St7wGeqfX90r+3ln5UeDcwp6PztarwCYn1FJrpE89HWUqiIgAiIgAiIgAgEQCL8xEoCQShIBBFISgRVPAZ82BA7+eVKhuKuAliuAmveejDtx5DnxrjcREAEREAEREAEREIHIJCBjJILq9cjRVHzxSzze+eKAo8Kn83/A3lkNgBVPAKmWUWIxT/IUxa9FR+Od1I/wzk+l/cr72+pjVkr9BZuA8hMBERABERABERABpxCQMeKUmgiCHKlWHh9/fxivfrDPEWHyBzuR8OuTuGZ3E5RK/sOS7vjfsv2XoMOiTzHg0zaWnPut4F/elX8fhbwjx5npVQREwLUEJLgIiIAIiMBpCMgYOQ0cnco+gcqF1mPi+TegU7XRyBd13BtyLLkgJmx4FP1WvIPtR6tkP3NdKQIiIAIiIAIiIAJ+CSjSbQRkjLitxhwurwcpaFvxVbx+fgvUKLraK+3qg+ej67L5mLWluxUnf4cFQX8iIAIiIAIiIAIikOcJROV5Ai4H4CTx6Q0ZV+9m3Fv9aRSIPmpEO3bCG9J7+Qf490gNE6cXERABERABERABERABESABGSOkoJAjAr7ekFrFlnnzWn+oltcbkgo1NS8YHbiZgGQXAREQAREQAREIIgH1EIMIMy9mVa7gZqT3hiSl5MfUTf3Qc9lceUPyYqOQziIgAiIQNALKSAREINIJyBiJ9BrONf1S0br8NExpcC3Se0N6Lp+DtzY/iGTkz7XSlbEIiIAIiIAIiIAIiECQCYQhOxkjYYDu9iLpDRld93b0OesxFIo+bNTx9YZsOFzbxOlFBERABERABERABERABE5HQMbI6ejo3CkEbG/I+SV+9p7bHF8dLvWGeHXQgQiIgAiIgAiIgAiIQOgJyBgJPXNXlhhbYDtG1r47jTckJTUa72zuia5L50PeEFdWq4QWgRATUHEiIAIiIAIikJaAjJG0PNz9KRU4t1oBXHBuTFBD93pz8NaFzXBx6YVePjuSamDc/rn4rdCT+N85JYNani1/2ZL5vOXpQAREQAREQAREIIsElFwEXEBAxogLKilQEQvHeHBf2xJ47oG44ISuSXiu7t24vdj9KBS1/7gYnmig1gDE3fkHHujVIjjlZCBvy8sLw7KvjperVxEQAREQAREQAREQgYgjEEnGSMRVTnYUSglW7/2f94BPagNbPz0pRpFqQLMfgPqjgOiYk/G5dJQSNGVySUBlKwIiIAIiIAIiIAIikCMCMkZyhC8CL07YCXx3K/B9WyDxhDcEHuDs+4DrVwJlLo5ApaVS9gjoKhEQAREQAREQARHIGQEZIznj56irC+SPQlROatT2hmyefVIvekOafg1cOA7IV+RkvI5EQAREQARCS0CliYAIiEAEEoiKQJ2CrtLkGfNQp3EnE7r0HYX4IwlBLyOsGfp6Q47uOiGKjzekXOMTcXoTAREQAREQAREQgbxBQFqGhoCMkUw4L/hxKWbNXYiFs8di5cKpKB9XGsPHTsvkKhed3jL/+NoQX29IoQqAvCEuqkSJKgIiIAIiIAIiIALuJCBjJJN6++KbX9H2hsYoG1vSpGx21YVYsmIddu7eZz679uWYJf/PXYCFLQHjDTmhSfXOwPWrAHlDTgDRmwiIgAiIgAiIgAiIQG4RkDFyGrKcjrVtx540KeJiSyE1NRU7dlmd+TRnXPTB9oZseOOk0PSGNJ4HXDIFKHDc8Dp5UkciIAJBJ6AMRUAEREAEREAEIGMkgEZQvVqFAFK5IImvN+TI1pMC296Qii1OxulIBERABERABCKIgFQRARFwJgEZIwHUy4ZNPh33ANI7Msn2hcfXhvh6QwqWAeQNcWR1SSgREAEREAEREAERcDGBgEWXMXIaVIULxZgF675JduzeC4/Hg7gyLpnKlHQY+LU38NXVgK83pEqb42tD5A3xrV4di4AIiIAIiIAIiIAIhJCAjJFMYHPBOnfTshesc0F7g7o1vQvaM7k8vKeNN6QO8OcrlhwnHs1Ob8jls4Ar3gNiylrx+gsKAWUiAiIgAiIgAiKQpwlwrTEfAWE/DoKPhsjTQAJUXsZIJqCaNKpvdtNq3KaPec4IF7Q/1qdDJleF+bSvN+TwppPC2N6QqreejNORCIiACLiQgEQWAREQAacR4KMf+AgIPgqCj4TgYDYfEeE0OZ0mj4yRAGrknvYtzTNG2LimjBkITt8K4LLQJTm4Dvj2ZhT4sAwKzKkEfFAhrTckfwlA3pDQ1YdKEgEREAEREIHIIiBtMiHAGTTr/v4Pd97SzKQsG1sSnEnDGTUmQi8ZEpAxkiEaF534qRPw74fAsb1AwnYg8eBJ4Su2BFqtAuQNOclERyIgAiIgAiIgAiIQRAJ85MOBg4fT5FjjjErgjBpO30pzQh/SEJAxkgbHiQ9ZeNu1/yjCGnbvBnb/4kfiaBys9zp21X8fu47FhlfGbDI6lpiCA/GJrpTdX5tITErB/sORo09ySir2HjwWMfVjqYM9B8L8fc7md8Vfe+NNwV+8W+MiSR+2M7Y3t9ZFerl5H+D9IH28Wz/vP3QMicmpEXNvO2j9jh61fk/dWh/p5T50JAkJx5IdVT+8PzEUL1bEPRscwTn/ZIw4py6yJ0m+otjV8jB2XZ+QLhzG0cp3ZS9PXSUCISag4kRABERABETA7QToGaGHxO16hFp+GSM5JF6mREEoiIHagNqA2oDagIvagH639NutNhDENsCuZFyZkqBnhMd2WL/xP/OIiMKFYuwovfshIGPEDxRFiYAIiIAIiIAIiIAIiECgBLhgveaZlTD9/S/MJVzQvmTFOvAREYCJ0ksGBGSMZABG0SIgAiIgAiIgAiIgAiIQKIHH+nQwC9brNO4EPhKi7Q2N0aRR/UAvz7PpZIzk2arPPcWVswiIgAiIgAiIgAjkNQKcjsVHQPBREAx8NEReY5AdfWWMZIeaw69JTU3Fd7+swNYdexwuaWDi7d57AG/N+gyHDh8J7AKHp4o0fRyOO8viLVnxJz5dsAjJySlZvjaaVftFAAAQAElEQVRMF5y22G0795j7gfQ5LSadFIE8QeDL737Dz0tWgf0EtyuccPQYpr33ecT0ddxeHzmRX8ZITug5+NojCUfR65HRGD1pJuKPJDhY0tOLxhvm+/O+xbg3PsD1HR4Bj3kDOv1Vzj1r6zPqlRl4d84C5wqaDclWr9vk+vo5eCgeL01+H0++MBVr/vonGxScd0m+6Gh8tnAR7rr/adDQcp6EWZMo0vSh9jQUP/7yJ/y6fK2rO4nf/fI7mtzaB5yicmPnR13f6eUA2JR35qF1p0fRc+AL+Oan5ScGKVhr7gv/bduFF197D/c/+hIWL1vrPgXSSbzgh6Vg/dx53zCMm/IB3Nw3SKdanvsoYyQCq9zj8aDZlRegyWX18fc/WxEV5d5qXr9xCz6Y/x0mPNMPU0YPMCPWbbs94dofOeoz9/Mf0fSKBhHT8mhgsbPbvf/zoJHFDolblZv31c/GeK9Vs5pbVThF7jKlS6D7Xa2w/8ChiPixjjR92IEa/uI0PPPy23j8uSnYvmvvKXXohoi9+w9izKuz8MA9bbD8q8l4ZnB3jJk0C8PGTkNiUrIbVEgj4xar497xgRH44tvf0P3OVmh1TSNMnDYH/YdNBAct0iR2wQfep+lFqFm9Ci6sdw6KFHb37k6cYTB5xjz0694Oc6aOANtf576jQE+wC6pDIqYjkGkvNV16fXQJgVV/bsInX/6MbtZNNKZgAZdInVbMpORkvPXeZ+bGWa9ODdQ4oxImPfsQHu3TARwROXosMe0FDv9k63ONZSiWL1saVSvFeSXmCNy7H33tOnczOxmTps3F2Ndm45lHe+CcGlVQsVwZr15uOuC0xtmWF67rHa1QoEB+xJYu7hV//cb/8OGn37uyM8929/rbn6BB3bPR8PxaXp3cehBJ+uzasx+9H33RMhQPY0jfjqhcoSyKFy3syqpJsgyOlJRUVKtcDvRe0aB/9bmHsenfbdao9fuu0on3tRcmzQR1eGPMQLRqdqkJb700GIULFTTThl2lkCUs+wS/LFll9QmuR/780VbM8T/qSk/w76vWH49wySvvx/yucGCvaJFCGPzAXbjqknp4bvw7rjR+XYI918SMyrWclXHYCPDmQtclPSN1a1UPmxw5LXjR0tX4bOFi4w159pV3zJoRj8eDSxrUxqD774TbjCzq88eav9H2hiZGl3z5jv8gLF62Bnc/OBKjrVHF5ye845obKaf/8Ufsm5+X442xAxFbqrjprHOv9ZzWfaiv56jhmzM/xblnVQW/M8csQzc6KsrUxRvvzEePAS/gqdFv4otvfg21aDkub/nK9Wb6T6d21yG/1ebYmc9xpmHMIFL0Wb9pC7o+9Jwx4Ec91sOM6NLrwwWwYcSb7aJLlSyGBv87G89anUF7dLpE8SJ4uOdtaH3tZdnONxwX/vzbKqz6cyN6dLghze8Mvz/XN70ES/5Yh8Px7pn+TO/bxLc+sgyqRqhYvgyOHDnmxbrwx6WWrptQyTKEvZEOP/jr7/8w+5NvcF/nmy3jMMZIGx0dhZtaXI5//tsBDh6ZSL24hoCMEddUVeCCcpoM5+/fcXNTcxENk54DR4MjH+x0mUiHv8QfScDr0z9B97tuwNezxljSppo1IzROrA+u+6M+k9+eh9taN0Fp60c74WgiCuTPj/FvfgSOwLW/qanpzHe943rTYXS6guxsdOn3LGhIDR94D+jp4Z7qxYoUdqX7f5XlSfxx8R/oeOu1ZppWQcubuGffQfR6ZAz+2bIDLa6+BJza0NRl0+vY7iZNm4PrmlxkeRYrYt/+Q+jSdxR++nWl05uYX/lyRx+/ReVqJNce3HXfcNSsXgm9O99ivvPsQNH7m6sF52Lm+aKjLcOjHc6yPNid+zwD/gaxuFo1q6FGtYo8dE3gb+jlF9VFlYpxfmU+diwJbjLqqc+OXftw03WXgwMt+w4cMnrxfjDtvc/R6bbrzO+PiXT4C7m/5TNjwlfcQjEFUSimAA4cjPeN1rELCMgYcUElZSbiH2v/NqNqTMeby+S3P8Hdba9F1Url4PF4cPuNV6PdDY3xpDWyO8wl83e/+m4JDhyKNzfPoidcsFwzUiGuNDg3lK7YlncNxBPPv3HK1CYaXJz+wHc45B/1oSg3NG+E5ORkyzMSjyHPTmYUJo16CN/8tMx0GDkybyId/LLC8u6ws0EP1S0trzSdWxq8K1ZvsEbXynhHqpasWIfhVnuLP3LUwdrAeD8o/43WD/VZZ1ZCQsIxbLBGrfs+MQ6db78ONOq/+v43a5S0tVc3pyoUbxnxHNW12z7bHY2qO29pZu4Fny1cZHV884HTHp2qg69cOdWHHZclK/5EwtGTI8G++Yf6ODk5Bf83+wvjZXvE8u4mJiajXfcn8PX3S/Dvlp04u3plIxLrb+xr72HeV7+Yz05+YZua//VxOenVeeKhTmh1zaV4ZMSr4LoLW3Z67HlfPmp5He04p74fOhyP8nGx5jvjKyPr5affVoK/Q25Zc8E+wTTL4Oh65/Veg4Oycxrqh599jxLFi5r1pb565vpxDgqwPaMcOKIB7JsV18hyUIy6+cbr2PkEZIw4v44ylZBTf+7oNQxvzvoMT415Eympqbi28UVWh/cIFlgu2A3/bMUVl9TD1LGPYKN1zFGSTDMNY4LtO/fijXfnW52/G7w3T4rDUcO4sqVM57dgwfzgXt6XXlAH9w4c7R2FYzqOct/z0LPYuHkbP4Y9UB/WzT13tDSd2WhrBJFTgV4c9gB63X0jFi1bjX+37gSnb3k8HrADyc4xf0TCLnw6ATiq9tV3v+Hudtfhwa5twGkM70x8AivXbgQXd7KOeAk7f2+8Mw8fffYDbu7yGAYMm3iK0ch0TgjfL/od7Ahy1JDyFCtaGM2uuhAzxj+Oi+rXMltH0ivCDjw7I29/8JXZVIEdZaZ3UuDUkZenvI8HhrxsOr3PTXjHDExwCp29JqZXp5tMO6TcjHvoyfHgLjv87LSQU304NZIG8V7LI+QE3bbv3IOlf6zDuBEP4sZrL8OYJ+8za+BenDwbazdsRtnYkkZM3sNooNjGiYl06AsHjSZYHl5OO6OInMrU6bYWKGl1cr9ftMLsDjbn8x9wTbt+4O9U89sfxhvvzDeDAEzvxFCpfBls27HbyO4r3/qNW8zUYU4HYkeY35+FPy4z3x/eG3zTOuX4I4t9iWJFcMXF//OKFGX9zvy3dRfen/cdOH2TU57ZkX9h4kww8Nib2EEH8dbA1oS3PkKdc86wBr7KppGMxi6Nrobnn2vWLbFumNbJ+qRRII9/kDGSuw0gJLnT8zH5hQHYtXu/8Ya8PPwB8B/nuU9991NMmjYX17Z/GLM+XghPlIenTNh/4DA499JpN9FylsExefQANG5U38jp+zL742/wr3UTpaFh2VzGm0Bvw2cLF5tkvCGxI9/08gY4o0p5ExfuF1sfdmwpS8EC+XF/l1tQ99wzwR1BWD9dbm9pRttYF5UqlAFd6rd0HYIZH351yg8i8whX4MLuPt1uNd42j+d4W+Io4VP9u+CC/52N6lUrGNG4wcD+g4fxxTvP44Mpw1C5YlljkDhxF5orL64HbozADjuFr1opDpznzvnu7Mxyu1VOn2Pngwt0OQ2F09NadRwEpxn27Mzyu3Nt44bmu/1Ev07g4lu2K3tNDI0q6sm4WXMX8BBxZUqZziF/7E2EQ15yok+85SWyp0ayjTpBJc7Xf+GJXmZhNOXxeDxmDdzwgV1RuXxZcM2IfQ/jfa3GGcenNzFu6sxPsXnLDl7mqHDr9Vfh9puaotvDz+HjL34y7Wjt+n/wnzXAcnaNKlhieUjpyaaOn1v3g/nTR1lxfzp6/dXNLa6wjMa/TGed3iwCp8H+mOXN5gDY+eedDRr69GrNX/CLGRAb8uwUsM0x7Z8b/jW/t0mWF5yfwxlua90E3FyEBoctBwcs/2/252h0YR00qFsTX3z7Kzr1eQbR0VGoYt3/+g19BZ87cH0cNw8YNuAeFCxQADd0fASzP/kWnDJMQ7j/UxPw18b/0LNDa7PBDbf7LRRT0PQDBgyfBH5/eM+zGejdWQRkjDirPrItzZlWJ/Chnu3AjiJ/0Fas2WA8JC9ZhgmNk4/fGmn9OOyybpZH0eC8mqaD++asTzHw6UmYZ7nYj3fuU7NdfrAvLFWiGDjC5psvb/TLV63Hi8N6446brwFvPiNemm6mAnA0m2m5GI+j3Pa0FMY5IXBkip3Z9LL47giSnJyCPfsOWgZlHB7pfQfoyeLNdrEL9oPfs+8A6Mlh55EGFo3gDrc2R8kSRc0ofDvrB5H1x8WF6RkE93PWc+MPMOVMfyXl5bqlNlZnq2qlcqaTxSmC7MyPGNQN7FRyK1OnjSKy08FpMkMf7mS2kPZ4PMboXWp1Cul9s9vhemuU99uff8e9HW8037X3P/kGHMD457/tcNJUmuzqQw8j67Rl00tM3fHYqWGT5cUtVqyw+a7QwGXHl1MgPZ7jBv9iy3s6x/Iy5suXz3EqeDwe637cFK899zD4rJQLru2GXoPGouudrcwINncJvLhBbbxkeX9ef/sTI/+lF56HxcvXmON4a7Sbxpb54JAXGo3PP34v3rO+E3xuCr0619810KyHGXDf7fjB8qZy3dW7lld41KM9MHvyMLOD2MS35oAd4wlvfoit23cjOir8XSx+fzgty0ZLTxbvWZxWyymoe6zfHA6IcQCG/QdO6abhSGOF97sky6BisK8P9zsHFrhO8bXn+1sG4zrccs8QYwhXtYyo6eMeA9f7TbA8dfzNveKiumhz/ZUYPbSXMVA4yBdu+VW+fwLh/6b4l0uxOSRQPq40Dh8+At5wOBpwJOEYOJ2ry+0tTAeRHZGvv19qfVGvsjqRB3HvI6NdsB+8B/Qq8ObKaTNvvjjIzH3/7fc/cdUl9Sw9DoGd4B2795qpQRy5Xrzs+A9eDnHmyuXs9M22fuw4lzfK+tF6+KnxuOHuQWh51yO4q/fT4PzqKpZHYceJ5w7wB5s/3LkiTA4z5XSa0iWLg14gGlhxZUqmmRawZdsuUwLPx1sj1t0eft7MkzeRJ14YzymFbK8nosL6xs4sf7g5fYsGFhcc84ePHZM+j48z88npPeEPNtOxE5ngkLUJ/sCxQ3Hw0GFzim2JUxiuvOR/ZmE7pzTwIZxlY0tYI77v4uq2fR3nlTOC+7xkpg+nenJqJOvknn6jsOnf7T5XO+tw/8FDpqNLw/g9y4PN0ezYUsWNkPxeTH57Hjrf1sJ4T/n5h8V/gIHHJlE4X06UXeOMSpg4qh9+/2oKfv54vPGeJiYm4UjCUTOt8+3xQ1C+bGm06/Ekpr33GRrWOxesm4HDJ2KC1Xnn/Y7t8kR2YX+jZ/3tVx7De689hZGDu2PB7LFgJzg6OtpM07y1VWPQaKGg+fNF44GubdC6eSNMsgwS3gtq1azGU44L3A6Xg5d3WYNFVa1BFg7wFbI8CI0bne+VtbhlGHPmSvs+OwAAEABJREFUAbdrXr3uH/OQxENWf8KbwAEH1IH18eOcV8wmN/16tAPXl676cyM4mDn04c6mTzPE8ljR4KLIxxIT+abgQAJRDpRJIgWBAKeS9O91O54Z9zauuuVB0zm3O4i84bMjcvXl9dH+pqtBL8LEUQ9h+cq/wA5yEIrPlSzoouUOJ5wTzx+u6OgocJvF2a8/ZTpUXIxX2voBnz/9WXzz/ou4r9NNeH7Cu2bBe64IlMNM2Xl/qMdtZl0CR603b9mJOVNHYMF7Y/Dkw53AUTZOo7ug3jmmJI5c93n8ZePdMhEOeuHCez5TgFMFOW/3f7VrGMORIrLDwTniV11az6wBYief05+GjX0LbbsPxacLFiHZ8got/eMvPPrM65bbfa/x3DGO14cr1D67Gh7v2/GEzL+hVMmi4DSThbNfRMe214LbGnvgMdsB7z9wyNSXvUtNuGTOqFx6SznqOWjEa2YksetDz+Kvjf+BnhJewylc5517Jp4d0hP0pE4Y2RfvfrQAXMvE804LmenD6We1zz4DDc+vZaY8cq2T7+iw0/ThPfjhe2+zvgfJ4AYK7FTZMs79/Edz2PSKBmZtXJuuj+PV/5uLdz76Gjd1fgzcwMQkcOBLgQL5jbeHaxXZYeeUwXcmPG6Mk0YX1gE77ev+/g87d++3vCljcEuXx4yOOPGPAxPhvA94PB7wd7Ph+eeaDi7FYqecXuB61j2On+1QumQxlCld0qwfubvddeDA2NAXpjrKy0hZ6b3ms1M6tGnOj2bqHwe97NkFjPzulxUoUrggGLdrzz5YGJA/fz6ecnxIsjw5ZaxBlf/Vqg7qef01l5jflXJlSqFCuVirj7MDj42ajNadHsW4KR+YtbWOVyqdgJH4UcZIJNaqpZPH4zEj05yeNffNkWDHqmfHG82e6XT5003LjojH47FSw3xB2bnnDZU/AE7dyYWjUddccQFu7Pwo7n/sJXAxcSpSzQ3VdzGex+NB/bo1zVS17Tv3Gh05ep9sdXrNBwe8sMPBDganzRQqVNC64XvM3vUej8fcND0eD+5q0wx0S3Pk+u0Pv8KGTVtw3R39jf6ci+0ANbwisB6mzf4cNBjX/PWPWUTNOeScf3zE8hhwZHe75eVhmgmj+prRrMf6dABHsvYfPGw6/RyJpL40ULiwmh49bwEhPqhhjfTSqGKxRYsURsLRRBy1Ar8nFcvHmh9nerW4g9CBg/Gm08URRqZ3YuAC1q9njcErI/ognzWS27X99aZtrfLZ1phtkbJzTjn15PbT/OzEcDp9vvz2N7Mwlx3gA1bbKl6siFU/BY0aCVZbnP3Jt+A90EQ45IXs2Zba39zU7EJHw/H1tz/B5BnzcM8dLY2UnBbI6Vucwkmjkc8nefCxl02nKsnqhJlEDnqhTh3aNge3MOe9mp4c3ve4zjE5JcVs3/5Qz3YYNqALOOWJG0dw4MLWhfe4Dvc/7agBJXpD+XDKH3/9wwya+OL+bOEi8xt7T/uW4AMSB/Rq7x2U8U0X7mOPxwN+v2H9u/B/55jfFdtzyNkU3JGzXeurjS4bNm21jKwSXj32HzhsDVR8bRmQ+6yrnfdX88zK5ru9zBpc9Xg8Zk3We689Ce7ytm7Dv+jc5xmzwH3c0w8iKsqDrg8/Z6Z6O0+TvCWRjJE8UN+8edLzUeecM8AFxJwHz44hO31Unz8QnB/asuklZvSHnZOvv1+C8O/kQunSBt5AOYrITlUHa2Sn8aX1EB0VZYwSTt3ifH77inUb/jM3U46GcJoNn6/w7S/L7dOOeq9zzpmgkXVbzyeNkdVv6HgzYnNt44vMDx5HrjkS9+mM54zX5+Get5sfCCcpwWmAy1auR/e7WuHpR7qCi6i5+Ltxo/rgjZ+dkJlzFqBKxTgzYu3xeECd+nZvC7a/16Z/jCTLWGRdcVSRI1qFYgo4QsXGjeqZtTwtOwzEw09NwMNPTvDqQQF37N5rGSfRpr3x84o1f4Oj1jSq+Nkpgd8ffh94P+D3nV5SbvhwQ/NGxrtIORn33sffWHV0rhkV5jQ0LkDOaCttXhOukJE+11x5gVcftid6UtjR51oMThH8ftHvKF2yeLjEPm25za68EBxEYv2sXPu38Zw2tDw8y63vFqebcHG1x+MxeZSPiwXv7w3+V9OsWWBHkcaWOemQl/Osext3PuSi9qtu6WO89RzwSj+d0+PxoHrVijgUf8R4E2jAcPvzptbgE6fdOEQdw7lPt1vNAu+HrPsAB1w44MVZBW/O+swYjmxrbJv05nMhOD3ADLwfJFv3OF9d6Gnhb7BvXCiPOVBJT07nvs+gadt+6Nb/eXCQpUmj840Ym/7dZn2XKpnj9dZg2N0PjgTvb071NNJQ5JStgcMnYfDI14znnYy5AycN3RuvuwzckKRqpTjce/eN5neXv1tGQb2EjYCMkbChD0/BvEGy49HUcvnbEnDaDL+sN117uVno6a9zwp0oNjtoJxeuHbmo/rlmzi7l+uan5abTznmu1Itu9IlvfYRWlouWC9n4w7d56w6MfGk6LmnVC6NemWGNdB9jUkcEjuBym1xOL3vwnjZmvch9nW8CF1bTOLQfyMeRRo+HXq+6Ru6M3M3h2M2l7rnVwWfBVK1UznTKW11zKYY+3Mk844brfNZv3IKvv19qfgior1HAemE8R7K5oxjjWVeVK5YFjRjrtCP+2LngjmHcHaz9TU0tD9YR2Au/KSAX5nMrU9bP/83+Ar0HjzVzyGmQ8bzTAjnzXrBv/0HQa8DRdo/HA1iC0nO66s+NZioNPVk04vlDzg4ldxK6d+DoNFNprEvC/mfrQy8In5vAAQuP53iHnTrElSkFjmR3tkZFm1x2Pp4dcq/pxIdd8AwE4PSYKy6ui8f6dET/e28H9Us4dszqFFY0HkRexg49BynOO/dMY7CwQ0sv5Cdf/szTjgoc+Hry4c5YPH+i2ZyD9+yPv/gR3e5sZe4VFJZGMLeir3P2GShSKAZcv8TtZ7+2Bsb4QEimcUrgWhGugeHi6K07dhuv2xeWN46G10X1a3nFpHEy5tWZeMC6pz/zaHfweSxvzvrU/FYxUZLlzXp2/Ay88saH/BiW4PF40OLqi/HZjOfx7qQnzGAX73EejwfcyGLXHu7SGYefl6yy7msvovPtLYwni8JyCuGwMW+Bv7/J6Ywsng9X4DOwPnxjODg1mJvzsL9APTb9u93o6vEcvzd4PB5wYJaDF3M+/8FMG77bMrY4iMbvV7jkz4vlRuVFpfOyzuxUcWSN7+TAUUN2njrddp3p+H73y+9mzmv6zolTd3KhDuz8znlzhJnm1P7ep8AFa+17PYVzzqqKW66/ymxx+tGn3+O15/qbOf8cdTy/zllY8vufZjoEb7jMxwmBN00+eG/ay4/i4vq1/RqHlHP1uk3obHWsqlUuZ7wOUT7uZv6oT5o2J+S7ubBzyxFoyucvzPv6Z9D7w/Ul9nnKSkOXPwYcoeMaGdaVbZjY6Zzyzu/NBf87G9NfGWI6hrZce/cdBNcrDRg+EZ989TPYUbn6svqmTdppnPjO+eNP9Lvb28Flh3by2/NwW+smZgpXZltpO02n2FLFvet8bNnYkf3os+8xbMw047Fzatuy5fV9pz70fDCOi79X/7nJLFxnR2mVdew7SMFBJXpFml7egMlNSLI6u+bAQS+U6fW3PwHXV3378+9mUIj68DeGncU2ra4yu7+9N/cbPPf4vbj/nlvAZxhxgMlBahgD8bKG54EGFY3HhISj4LoKLvqmnFxvRQ/jkL4dQcOST6HnIvevrQEZ/u4yDb1dHJW/7cYm/BjWQIOX92/+BtmCsD3x9/HTrxdhxIv/ZxnxPc3zcbZu342OD4zEL0tXgzMSPvnyJ/R+9EUz88K+NtzvvFdzZkHPjq3N2hdupuCxfic5MOYrG6cXc20tp3nTYBx0/52Y8OZHeNPycvmm03HuEpAxkrt8HZ87b4oXN6hlRqF503nv44WmI8IfQQpvd044esDRLU5z4MgBvSf0pjCNEwJvpEP6dAB31+Cahecf74VHH7jL6gwCb733GRpZPxrs7FJW3nD548C52DXPrOSdC8tzTgmcnsTOvb+Ra/6Yn87dbBuUvqPDTtDrAWt0sHeXm606OT4qRZkWL1tt1oxw/RLnkKevK6ZxYuD0C4/nuB7sSHF0lKPUXCTJRZN8aJoT5c5MJq71oReEU4T43edOO6fbSjuz/MJ9nvcrLpA+z/LaTXt5sJl6Fm6ZslP+gUPxZqMEdmxHT5qJi6+/F3wuBI34GmdUNJ336R98CdubyjJ4b+94/whwt0F+dkqwO+CTnn0Yu/cdQNN2/czubVPfnW9G3Pkden/et2aKIHd74yj3c0OOe7I4yk2ji2vonKKPLQc3teC9uV33oeCUrWV//IXKFcqgQd2z7SRISUlBUlKS8Yzw+zV+6oe48+am4ICaN5GDDpKSkrFz1z7EW4YWPaN1zz3TyP7We58bHS+2vEDNr2qIEYO7Ge/Q4uVrHSR9WlE4PZWbWnA6MI0s+yynF3OtD6ej7ty9D+fUqAJO8/ph0R/gWkY7nd5zl0BU7mbvm7uOnUjg7OqVzRePnflkaxTtdDu5UH6Ozg0bcI/ZoeaWe4Y4aicXj8djfrCvbdzQ7G/Pzjx/+Lg1YYdbm6fpBPMHjZ1IdrqoFwM78YznsVNC+pFrynU6d/OlF9QGb7Y1z6yM31evh9NGEym/HfhjPNlnFJ47bPGH4e5216WpKzu9E9+Tk1PwttUJXLxsDV4c9gD697rdO+3EifJmJhM7TuNH9jUjiYDHGOocSeToZ/qttOHgf/xuL/xxGbj4ucXVF2H00Psct8YqUHzceKPPkJfxuuVNYP28P3kYOOWJDxi1Bxze+fAr0ADm2hI7X0535KBSnXPOsKMc8f77qvVoa3k/+NtDr9z86c9i1qtP4v0pw83DINdv3IK5n6edwsW1jg89OQH9hr6ChT8tQ8+BL4BGGT2rjlDKEoLeEfPMkdefMuvJeH/jlEHb08A2yWlaNDxKlSwG/tasWLPBbFDQsEVP8JlZvMbKyjF/bD98hsrYJ3t7vz80cpf9sQ4vDX8AK9b8DQ5OLvl9nblXxMcnGGOFA30fzP/OMXpQEE6hfbhnO8toikHjNn3Qvtcws/ENjfXrm14KrqPjFMfOfUdZem0wm3ywX7Ry7UaTlg9XZD4KuUMgKneyVa5uJEC3ZkY7uRSKKQiOmn77y3Lry1zQzPvlwuOXXp8Np91Afdlzwd1dbZqZH2o7njcV7ujERXr8AWE8b7Dc5i8lNYUfHR0ycjfT+Pr8m8XgDZTbZv706yqz69YX3/7qWH241SfXMLENTfYxTBwrsI9gNPQefmo85n7xE6a9/CjcMC3LR/xMD+n9oZfx5SnvmzVMbF/XN70E9lbamWYQxgR8tgXvV+wcumlalj9kXCj87JCeYKfo5i6Pgc+4eW7CO2b6EjuL/O6wQ8XvEr/7zIMj81yT0eeC9aAAABAASURBVLPjjWY0fsCwiah7dWfwAX7sELNjzHThCFxzwMEhu2w+94Lealv2JSv+BKeq1vYxombOXQgOVgx9qJPxnswYP8RsTf2rNQhg5+OUd07V8ng8uMQaGFpvGVZ8HkySNdA37+tf8NGnP4C6c0CJv0Fjn+ptpg5/+e4LWL/pP3xs3UucooctB+uF3337M9tOjNUf4HNYBj9wp5lKxwEZtsHzzzsL1Hma5TkZ8+oscNMLevF9PRF2PuF4Zx/nkd534LsPX8arzz5kjEbuLMh7HWd+DBvQBUP6dACNYW6Okz9/fnAWyH9bd4JTwK+46X6z7ocMwiF/JJcZFcnKSbesE8hoJxfeJLs9/By4GwgXtHbv/zzo0vQtgSN4ydZIsW9cuI/5NNkbr70sjRjf/rQcFeJi0fD8Wt54jiLai6Z5o3n7g6/Mg634Q+9N5JCDjNzN7IBMt+R+sOutZpEefyi46wtHqDgFzyHie8XgD4O9fum7X1aYETVfT5U3oUMPuLnAkL53g9usclTaoWLmSKyMttL2eI5PUctR5rl4MdtWz46tre/4ublYyqlZ51YMO+tjnrwPE0b1AxdNv//6MLOFNsuLjo42nqzfV20w6y+SrI7v65YX5eIGtc2W7uwk/rNlB7794CW8Pf5xzJy7AG+8O99833ivc9o27nVrVQe92Ryl5n2L02e+/O43cIrns+PfwVNj3gJ/a3gP50J4MuD0rfS/R4wPZ6AHZNSj3cHnRdVv1tU8G4ZrErjhgO+ugpSR64I45cnJz4yhnAz06nAqHTvsydbvfYW40mDbfGfi4yhXtjS4BvCWlleYhfB89tQ3Py8HtwrmtU4JNLDsgcjLLjwP9KL+9OtKI16NMyrh/8Y9Ct77vjuxhvYDy2u34L2xlvf7fnBq3YZ/tpq0egkeARkjwWMZMTnxS8o1FY+d2MmFI/Efff4DBt53B0Y92gMfTX0avTvfDLpib2jWyPKUxICeBRop31qeE6eDOHj4CGJiCiBf9PHmn37RdEpKKs6ybkicetOq4yDzYC4n6ZTP6nw8nM7dTEOEBtT5dWrA3t6YHY1Vf25E5QpxxoXuJB3Sy8KF7a94pwelP+vcz6VLFnP1tKzMyEZb3xFOBfLdSpvtL7PrdD74BDwej/Hw8vkqNITtEjgNaEjfjmbKyRU3PYBr2j0ELmy/4+am8Hg8ZuBl776DWLxsrXVcGsMHdkXxokVADzGNlq+/XwJOmbLzC/d7rZrVMH5kH/DexUXgSUnJKFSwALgwf9rLg9H8qgvBZ0Nw5636dWuaqaiDRr6Glya/b6Y+OckosTu2K75+Ax+98bQxjuk5+Pr7tLsK0nNAj9BF1gAZ79vcdOGFiTPBhxM7SR+2DX7/+/e63fJUrcFd9z+N2Z98axmPm8xjARb7rAH0eDzWb09Z0Ev//rzvzEMG+w+bAOrGfOxAfWnU2J+z+J7j5PTCDRt4D0a89H9o12Monp/4runPcGogjag7b77Gu8FHbKkSiD9yFFwX1KB5N7PNO71cvkLwczj18ZXFTcfHe2NukliyhoxAbKniZvvLQlbH/cwq5fHdot/Nsy88Ho+5+bDD3vTEFsH0LGxOt3WuUxd/tWhykXVD3IJOfZ4xO2YMG/sW7AXunIPMkTh26EcM6oYXnugFupud9oA0jvz6ups5ZeiXJavA/dP5Y8FGwmkqvyxZjZtbXM6Pjg7s9LKdOVrIPCwcO7wXndhKOw9jcKzq9Jw8//i9+OnjV9Cq2aXoftcNZgoK72XsbA19qBNGjXvbeHsrlou1Rn2vQv58+cyUk/gjCWYaHjuFTlHwzKoVwF2NuAMVB8c4VY3brXo8HnBB+7sTn8CLT91vBo0+W7jI0iUa7PRyd6dbuz0BGipO0SW9HPO+/tnsOkUjyz73xTe/WnVwAJzaxV2cej/6EqpUirOMxsLgIJ/TptqyvU20vHSDet9hjOBoa4CM7Whyuqm27JjTq/XI/Xdg8gv90bDeueg1aKzZ4dLWnbMu+jwxDkcSjtlRIX/nwvwPLWNx5ODuxuhl34ftis/Gsvs4/H5wV77LLjoPv8ybgB/nvmINxBbEs6/MQJLljaTQ3FiBs0bojeRnhcAJyBgJnFV4U4axdI/HY3lCbkHhmIK45raH0Oz2hzHmtfdwzx0twU6x7VlIv3UuH5RGIyWMovstmnvEz5jwuFlsTHc/n03Aebx7rNHDu+4bjlvuGYJr2vUD52Z7PB5jkPFHnZnFW6MiNFh47ISQP9/xKRp8VsR9lreKUwMoF2V8/e1PwN12fLfS5TkFERCByCTAgYiHe96Gdq2bgNvk9hv6CrZs24VLL6xjptJwCg2nNFH7pX+sszrx+fC0Nejy8pT38e6cBYx2XOAGCr063WS2W+UWrJT/WGISOJ2L07TST02985Zr8L41Wk+DhGsGk5NTHKUTdxV8cfj9GDB8EvoNHY/eg18Ep8rxmUwcVOIDX7kegx6wO29phif7dwY9C/GW0egkRaItr+n/atcApwJzByo+3JHy3dC8Ed/MNMC3P/gSVSrGgc+M4mYs119zKSqWjwV3H2QizqjgowVaW9eEezCK+tD4rX9eTRw4GI8vv1tijHr2cSjrqj83gc/D6njrteD3jO2Sniw+pJNtjMbKrLkLQEOaHjteoxA4ARkjgbPK0yk5p/UJa3Tt54/H44Eut5g1CRfVr2VGBN7KYOtc7kXOEQYngmMnng+o6nJ7C7wyog845/+r735DqZJFzYLChbNfBLdqfPKFqfBY/9mhpyt94PCJZvckp+nEHy9OdbLlWmy5y+nN4Za5Ho/HjtZ7FggoqQi4mQCfQXTVpeej5yNj8N0vK8w6C1sfu9PLzT24VmH6K4/h9huvtk877p1Tt/jsnvJxpfHI05OwdMW6E53dr+A7NTXh6DGsWL0BXGvyzY/L0f+pCbhv8FjjibCV+nPDv5j18ULz22XHhfqdvz2zXh2KG5pfijatrjSbQjDuh1//MB6ejrc2R1/LW8ApQzS86EXhABONr0dGvGqmEYVa5szKu6FZI4yzfkvtzjuno7Hz7ruBBL31HAA868zKpv6mv/8FKlcsa4yVzPIP5Xn2d157/mHwmVIsl+y5kJ2DezXOqMgo06ben/ctWjS52EyDto2VezveaBn50SaNXgInIGMkcFZKeYIARz64JSNHBzLaOpc/BolJSShdsri5iqMGfILrNz8tB0cRTKQDXji6QU8JRSlapDASjibiqBU4SsIRnPz584G7bvEG+90vv+O3FX/i7fe/xCWtepn5ott37jU3VV7vpPDv1l3o0aG1mSPuJLkkiwiIQGgIeDwedGp3HcYM7YU5n3+P0a/OAr0mHLiYbXWiOPXJnoISGokyLeW0CThlhvq8M/EJXHVpPWN0/JJuauqPv67Ezj37wek29DRMHj0A+w4cwrKVf5m8E5OSMWnaHHCgLDoqvN0f6tOkUX0w2GuAaHSwfujJmj7uMbPV8cNPTgANruJFC2O69dvz82+rwKnD9Cg46Vlf/M20vRtJycngIOU1V15gNlEgfHp2uPi7Tcsrze8SjZX3532HxcvW4MZOg+GkXbcor2+ggbttxx7caXmqPJ7jg3vzvvoZHo8H/A6xXdFYYVvr1v85aNctX3qBHYf32xiYjErlYAJ0g3N0jZ4FXzF5k0xNhXlwVYI1WvXCpJl48oU3UbpUcfCm5ZvWKceNG9VD1UpxaNlhoDE0+CNQxXIxc9ctupNfn/4JuL//ZzOew9ezRuPqyxqA09DoYneKDrYc3EXs2sYN7Y96FwERyKMEapxRCXxoIEfiOfWHD1Dk7kEdbr3WTLN1K5b0U1Pp7Um/4Jij8NyApfSJQTEOKNG7wGlsHs/xTqWT9OdI/NffLzEPFOTv5PVNL8EX774AbofMDjGNr5effhBcG8jPs+YudJL4Xlk4UMmt/+kV8XiOc/7quyXWYN8xXNv4IrDzzimDtzh81y1boQZ1a4IPfbRnenBtCKc13nNiqjrbFR+wau+6xWewTLSMXufvumVrGP53GSPhrwNXS8BOb/qtc6kQ51zS67Bn30H0fvRFM3+ZO6FwoRjPOzHQ+/FU/y744p3n0f6mpjgcfwS2y5VGR1yZkuCPOWVn2pZNL7b02mYMLMYpiIAIiIDTCXAzAo7EL7e8BRwocrq8GclHD4Lv1NTPFi4CvQ0cqeY19MbTe8CHPp5zVhXQWOEDYc+pURUr12w8ZWt6XhPuUK92DbS/+Rp06vMMuD6G616SkpIQZXlxKHurZo3A31DqPuqxHsZICbfMGZVfqkQxUx88z8G86R98iXvuuB5se4uXrTa7pdnTiCtXKIu7212LpVabjD9ylJc4LvB7Yws157MfLI/PGeBAJdtVeiP47OpVULpkMbNey75G76cnIGPk9Hx0NpsEduzeiz/WbEDXh541c2DD/QTkrKhBQ4MjVNNfGYIaZ1Q0o1Qff/Ejut3ZKs02rpyKRrcsvSl2/qvXbTI71Lj5R97WRe8iIAKRR4CDRJxmu33XXgwb81ZY104Eiy6nBVmOePTqdJPX28M5/NziuKPlAeJI/WeWscK1gk7edcvj8YCDe3yOTM0zK2PzfzsQE1MQHHnfsWsfbrrO+Tsj+qvTksWLggN9HMyLP5KAyel23eI1y1euR/WqFa36K2g8J9w9jQ+MZHqed1Lo0r4l+B1ie2K78jWCKeeW7bvAAVkajfQC0ajkd+3jL38y3iGmUUhLQMZIWh76FAQC7Ij/smQ16EYfPfQ+0FXLL20Qsg5pFnwqq8fjAfe6b3ZVQ3D3Fl8BqGdiYjLiYkuZdTDT3//CLJYsWLCAWdDmm1bHIpDHCEhdBxPg1qzDBnTB0490NTsDOVjUgESjscEF+PQs8AJ2ADmHn2sW7AGl6R98hQe73mo2Xxn8wJ3gLlBzP//RkcYYvQd8uCU3UYmPTwB32OLaRXuaEHV0U+CUs7OrVzYLu7nr1pr1/5j1MLYO3JHz828W49rGDc1jA1rfPdjo/MH879Cm6+PGGLPTOuGd/RmuJ91/4DA+/vJnI1LyiV3b2Pb4oMuG55+LEsWK4P5HXwSn011Y7xz8vmq98XpxhztzkV68BGSMeFHoIBgEOG+y28PPg+/TX3nMcmOeG4xsw5pHowvPQ6+7bzSL1XwFOXYs0YxyREV5MOTZyZjz2Y+YMnogrr6s/ilpfa/TsQiIgAiIQO4R4HbtJazR+DtvaWYKedsyRLgIvF6dGuYzXxITk/hmAjuQTh2J585Or78wwPpdaWBkzfjFHWe469bLwx/Ao8+8bp7zNXPuQnDnsFtbXYVzz6oCPhKAm8eMGNwNfHYOBzRpWNrb6ztJS9bNWy8NMltn39bzSasfMAW39RgKrlW6z/LSzf/6Fyxauhrn1zkLTax+weAH7gKfkzN/wSInqeEIWWSMOKIaIkMIztFduXajGXniDYSjb5GhmX8t6DbnYsieA0dbruUYvDGBwYTeAAALCElEQVR2IOiW9Z9asSIgAiIgAqEgQA/C4307midnr1i9AT8sWoFOt7XweoH4dO1PrQ7hZQ3rYt2Gf+H0kXjuUkXvQijY5XYZ1KNB3bPx6vP9sXffQaz96x8MuO8OdLbq5/dVG8wAX9PLL8AdvYbh/XnfglO8uBnOHistZeNUaG6Qw2MnBI/HA+7yxodAXn5RXdDg4CYD0dHR+Or7Jcb7yAeM3nnfcLDNcRc7tj/KvmTFOgwfO8081Z2f83KIcqPyktmZBDweD5pfdSHuuLmpccc6U8rgSEWXLLeLPJaYiEd634FHH7zLGCTByV25iIAIiIAIBIMApwufd251vPp/c8FOLKfXvjnzM7CzePlF57lqJD4YPJySR4W40uBUuSGW0XjFxXXNbIKEY8fMgB77EO+99qTZlrldj6EoFFPQPAvsn/+2o/+wifhh8QrQU8IBUKfoU7VSOTPNjNOxOI0LSDXTtStXjDMbDbz54iAsWfEnpsyYh8aNzjdG1xvvzLN0+QPPvjIDeX09iYwRp7RkyeEaApwnOmD4RHBHjbdfGWI8QR7P8e0LXaNE1gRVahEQARFwJQF6q58a0AXnVK+CJrf2RcMWPbBizQaMHNwNGzZtNZ3C043Ec8oNB59cqbzLhOauWpv+3W6meXOjBa43nfnqkxh0/52mY8/pdvSUfL/oD3S4fwR6DHjBGJhOVJMb4Zx7VlXMmrvAtDEucqfX5NMZz+G8c8/Egh+WWsbWYUx4pi9uv+lqfPTpD45bGxNKrjJGQklbZUUEgT83bEbNMytrWlZE1KaUEAEnEpBMwSTAkWo+q2Px/IlY8fUbmPTsQ+A04sxG4rklbZe+o/DtL8uDKY7yyoDAWWdUwvXXXIquDz0HLl7ftnOP2SK3aqU4y6uwDnyo5YhBXcHNF+g5ecQyUtjJzyC7sEezzaWkpKJd96HgBje//f4nihYuBA5oclOCjm2bg8YyjZbXnn8Yza68MOwyh0sAGSPhIq9yXUuAu2T07Nha07JcW4MSXAREQASA043Ec2Sez5favHUHRr40HZe06oVRr8wwo9xilzsEPB6PmeY9fmQf/L56g1nkzulYnFo39d35ZtvjqpXKmcJZP9WrVjDHQXnJhUzoHaHh9NLwB7B33yFw04To6CiwXfk+tywXinZdljJGXFdlElgEREAEREAERCCnBE43Es/tZj/69Hu89lx/fP7O8/j4rZFmVyTfh9/ltHxd75/AmZaR8US/uzH5hQEoX7a0mdK0/+BhtGl5pf8LHBzr8XhA70fvLjfjkgtqg9PQuKV0z443pnlumYNVCIloMkZCgtlRhUgYERABERABEcjzBDwe/yPxScnJeOu9z9Co4XmofXY1w4nTuq5t3NAstDYRegkZgXJlS6FPt7bg81dCVmguFVStcjm8PX6It13lUjGuy1bGiOuqTAKLgAi4i4CkFQERcDKB9CPxy1eux+p1/6DDrc1lfDig4rgVcIO6NR0gSXBEKFyooNpVOpQyRtIB0UcREAEREAEREAEXE8ih6Os3bcFdbZqZ7WRzmJUuFwERCICAjJEAICmJCIiACIiACIhA3iDQ7obGZrF03tBWWopAzgnkNAcZIzklqOtFQAREQAREQAREQAREQASyRUDGSLaw6aK8S0Cai4AIiIAIiIAIiIAIBIuAjJFgkVQ+IiACIiACwSegHEVABERABCKagIyRiK5eKScCIiACIiACIiACgRNQShEINQEZI6EmrvJEQAREQAREQAREQAREQAQMgTxujBgGehEBERABERABERABERABEQgDARkjYYCuIkUgzxKQ4iIgAiIgAiIgAiLgQ0DGiA8MHYqACIiACIhAJBGQLiIgAiLgdAIyRpxeQ5JPBERABERABERABETADQQkYzYIyBjJBjRdIgIiIAIiIAIiIAIiIAIikHMCMkZyzjDv5iDNRUAEREAEREAEREAERCAHBGSM5ACeLhUBERCBUBJQWSIgAiIgAiIQaQRkjERajUofERABERABERCBYBBQHiIgAiEgIGMkBJBVhAiIgAiIgAiIgAiIgAiIwKkEThojp55TjAiIgAiIgAiIgAiIgAiIgAjkGgEZI7mGVhmLwOkJ6KwIiIAIiIAIiIAI5HUCMkbyeguQ/iIgAiKQNwhISxEQAREQAQcSkDHiwEqRSCIgAiIgAiIgAiLgbgKSXgQCIyBjJDBOSiUCIiACIiACIiACIiACIhBkAjJGggRU2YiACIiACIiACIiACIiACGSNgIyRrPFSahEQAWcQkBQWgcEjX0Odxp3ShAU/LrXOHP+zz193xwDs3L0P8UcS0KXvKNhp+G6f4xVMP3nGPB6Cx6fL2yRK97Jy7UZc274/+M68WRbLZOCxnTfPt+0+FP/8u83Ik74cfmb5lJnyMS8Wxet5zjcwjucUREAEREAE3ElAxog7601Si4AIiABGDOqGlQunesO4EQ+i9+AXvcYGzy+ePxEVy8Vizuc/+iXGc0UKxxhDZduOPd40vPZ0eXsTZuGgerUKJvWO3Xtx8FA8ChWKwZQxA73yU9aL69cC9WD5JnG6F55nOsq2cPZYzJq7EDJI0kHKlY/KVAREQARyh4CMkdzhqlxFQAREIOQEmjSqjxuvvQxffPOrt+zCVof/sovqYv3G/7xxGzZtNcf2u/lw4sU2GE589L75y9t7MoODLdt343B8ggk89k1mG0G+cVk9LhtbEm1vaJxGt6zmofQiIAIi4EgCeUgoGSN5qLKlqgiIQOQTqHFGpQyVpGFSPq60Oc+pUz8sWgF+ZjyNhvQGg0no83K6vH2SmcO42FIoVrSwOf5j7d/Yf+AQGMcIf0YQ47Mb6NGhPtm9XteJgAiIgAiEj4CMkfCxV8knCehIBEQgGwS4roIhq5eOnjQTDVv0NJc91qeDeecLjQfbYGC+DIwPNNQ55wx8NuM58J3X/LtlBxq36WOmjo0Y3M0bz3O2EcRjBREQAREQgbxLQMZI3q17aS4CIpAHCTS76kJcXL8WuO6C6zXoFSEGei+KFSmEM6uW58ccB+ZTq2Y1s/6D6zs4zYuZ0oNBjwzl4GcFERABERCBvE1Axkjern9pLwIikMcIcAE4VR4+dhrfTODuVoNHvIYObZvDNk7MiRy8MB/mx3yZv52VXa4thx2vdxGIaAJSTgREIEMCMkYyRKMTIiACIuBeAvRAcDvdOo07gdOybE1oJHC3Kq6z4DmGdj2GgtOobO+FnTan78yP+TJ/lsPAclk+5chp/rpeBERABETA/QRywxhxPxVpIAIiIAIuIMDtbxl8Rb2nfUuz5S87+5yGxSlSDL7p0p/j+SaN6vtmY/LwvYYn7bx5HGhgvszfDpSJ5fu7nvE8z2t4nrtlffr2s7A/s3yeZzqeZ/AXx3gFERABERABdxCQMeKOepKUInAaAjolAiIgAiIgAiIgAu4kIGPEnfUmqUVABERABMJFQOWKgAiIgAgEjYCMkaChVEYiIAIiIAIiIAIiIALBJqD8IpuAjJHIrl9pJwIiIAIiIAIiIAIiIAKOJSBjxHFVI4FEQAREQAREQAREQAREIG8QkDGSN+pZWoqACGREQPEiIAIiIAIiIAJhIyBjJGzoVbAIiIAIiIAI5D0C0lgEREAEfAnIGPGloWMREAEREAEREAEREAERiBwCjtdExojjq0gCioAIiIAIiIAIiIAIiEBkEpAxEpn1mne1kuYiIAIiIAIiIAIiIAKuISBjxDVVJUFFQAREwHkEJJEIiIAIiIAI5ITA/wMAAP//DAwlJgAAAAZJREFUAwDB1iUrtdiCKAAAAABJRU5ErkJggg=="
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import plotly.graph_objects as go\n",
    "\n",
    "# Load the file directly from the current working directory\n",
    "df = pd.read_csv('amazon.csv')\n",
    "\n",
    "print(\"Amazon File loaded successfully!\")\n",
    "#print(df.head())\n",
    "\n",
    "shape = df.shape\n",
    "print(f\"Rows: {shape[0]}, Columns: {shape[1]}\")\n",
    "\n",
    "total_rows = len(df)\n",
    "print(f\"Total Records: {total_rows}\")\n",
    "\n",
    "#### Data Cleaning ####\n",
    "# Remove duplicates\n",
    "df = df.drop_duplicates(subset='product_id')\n",
    "total_rows = len(df)\n",
    "print(f\"Total Records after remove duplicates: {total_rows}\")\n",
    "\n",
    "# Cleaning discounted_price Column: remove Rupee currency , remove comma and convert to float\n",
    "df['discounted_price'] = df['discounted_price'].str.replace('₹', '').str.replace(',', '').astype(float)\n",
    "\n",
    "# Cleaning actual_price Column: remove Rupee currency , remove comma and convert to float\n",
    "df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)\n",
    "\n",
    "# Cleaning rating Column: remove \"|\" char and convert to numeric\n",
    "df['rating'] = pd.to_numeric(df['rating'].astype(str).str.replace('|', ''), errors='coerce')\n",
    "# Cleaning rating_count Column:  remove comma chars and convert to numeric\n",
    "df['rating_count'] = pd.to_numeric(df['rating_count'].astype(str).str.replace(',', ''), errors='coerce')\n",
    "# Cleaning discount_percentage Column:  remove % chars and convert to numeric\n",
    "df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype(float)/100\n",
    "# Create a new Category\n",
    "df['main_category'] = df['category'].str.split('|').str[0]\n",
    "\n",
    "#save the results to new csv\n",
    "df.to_csv('amazon_cleaned.csv', index=False)\n",
    "print(df.head())\n",
    "\n",
    "\n",
    "#kpi\n",
    "print(\"KPI:\")\n",
    "# סינון ה-DataFrame לפי הקטגוריה המבוקשת\n",
    "computers_df = df[df['main_category'] == 'Computers&Accessories']\n",
    "# חישוב הכמות\n",
    "count = len(computers_df)\n",
    "print(f\"Number of products in Computers&Accessories: {count}\")\n",
    "\n",
    "# 1. סינון הנתונים לקטגוריה הרצויה בלבד\n",
    "computers_df = df[df['main_category'] == 'Computers&Accessories']\n",
    "\n",
    "# 2. חישוב הממוצע של עמודת הדירוג (rating)\n",
    "average_rating = computers_df['rating'].mean()\n",
    "print(f\"Average Rating for Computers&Accessories: {average_rating:.2f}\")\n",
    "\n",
    "### 3\n",
    "\n",
    "\n",
    "\n",
    "# 1. הכנת הנתונים - וודא שעמודת התאריך מזוהה כראוי\n",
    "df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)\n",
    "df['month_num'] = df['order_date'].dt.month\n",
    "df['month_name'] = df['order_date'].dt.strftime('%B')\n",
    "\n",
    "# 2. סינון לקטגוריה וקיבוץ נתונים (אגרגציה)\n",
    "comp_df = df[df['main_category'] == 'Computers&Accessories']\n",
    "monthly_stats = comp_df.groupby(['month_num', 'month_name']).agg({\n",
    "    'product_id': 'count', \n",
    "    'rating': 'mean'\n",
    "}).reset_index().sort_values('month_num')\n",
    "\n",
    "# 3. יצירת הגרף\n",
    "fig = go.Figure()\n",
    "\n",
    "# הוספת העמודות (המלבנים) לכמות המכירות\n",
    "fig.add_trace(go.Bar(\n",
    "    x=monthly_stats['month_name'],\n",
    "    y=monthly_stats['product_id'],\n",
    "    name='כמות מכירות',\n",
    "    marker_color='royalblue',\n",
    "    text=monthly_stats['product_id'],\n",
    "    textposition='outside' # מציג את המספר מעל המלבן\n",
    "))\n",
    "\n",
    "# הוספת קו ממוצע הדירוג על ציר Y משני (ימני)\n",
    "fig.add_trace(go.Scatter(\n",
    "    x=monthly_stats['month_name'],\n",
    "    y=monthly_stats['rating'],\n",
    "    name='דירוג ממוצע',\n",
    "    mode='lines+markers',\n",
    "    yaxis='y2',\n",
    "    line=dict(color='orange', width=3)\n",
    "))\n",
    "\n",
    "# 4. עיצוב הצירים והגרף\n",
    "fig.update_layout(\n",
    "    title='ניתוח מכירות ואיכות: Computers & Accessories',\n",
    "    xaxis_title='חודשי השנה',\n",
    "    yaxis_title='כמות מוצרים שנמכרו',\n",
    "    yaxis2=dict(\n",
    "        title='דירוג ממוצע (0-5)',\n",
    "        overlaying='y',\n",
    "        side='right',\n",
    "        range=[0, 5]\n",
    "    ),\n",
    "    legend=dict(x=0.01, y=0.99),\n",
    "    template='plotly_white'\n",
    ")\n",
    "\n",
    "fig.show()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0622953d-bad5-47f2-9b25-0836080ffbf6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45f769bc-2aba-4491-966f-9eabb629d670",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-ai-2025.12-py312",
   "language": "python",
   "name": "conda-env-anaconda-ai-2025.12-py312-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
