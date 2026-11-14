# Difference-of-means steering at the final token (exploratory)

Items: the item file is the set of accepted pairs.

## Llama-3.1-8B

* A1: cosine(moral stance, norm stance) by layer L7: 0.68; L15: 0.82; L23: 0.93
  * layer 7, stance: moral +0.9% [+0.5, +1.2 at +1]; norm +0.3% [+0.0, +0.8 at +1]; descr +1.2% [+0.7, +1.8 at +1] (of the gap per step) -> not shared
  * layer 7, category: moral +2.6% [+0.2, +3.1 at +1]; norm +12.4% [+9.3, +15.7 at +1] steerable, expected; descr +9.0% [+7.5, +13.6 at +1] (of the gap per step) -> not shared
  * layer 15, stance: moral +39.6% [+25.9, +68.5 at +1] steerable, expected; norm +46.3% [+34.8, +49.8 at +1] steerable, expected; descr +46.8% [+29.9, +44.2 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 15, category: moral +4.3% [-7.4, +7.3 at +1]; norm +16.8% [+13.6, +29.7 at +1] steerable, expected; descr +15.9% [+14.6, +31.3 at +1] steerable, expected (of the gap per step) -> not shared
  * layer 23, stance: moral +78.5% [+56.7, +154.9 at +1] steerable, expected; norm +88.5% [+82.2, +108.5 at +1] steerable, expected; descr +108.3% [+96.2, +142.5 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 23, category: moral -0.2% [-5.5, +5.1 at +1]; norm +0.1% [-4.6, +8.6 at +1]; descr +6.7% [-1.0, +14.9 at +1] (of the gap per step) -> not shared
* B: cosine(moral stance, norm stance) by layer L7: 0.66; L15: 0.81; L23: 0.86
  * layer 7, stance: moral +8.9% [+6.1, +13.5 at +1]; norm +7.4% [+5.2, +11.1 at +1]; descr +1.5% [+0.4, +2.9 at +1] (of the gap per step) -> not shared
  * layer 7, category: moral -2.0% [-3.6, +0.9 at +1]; norm -3.8% [-4.1, -0.9 at +1]; descr -1.5% [-1.8, +1.0 at +1] (of the gap per step) -> not shared
  * layer 15, stance: moral +82.0% [+78.7, +144.5 at +1] steerable, expected; norm +76.5% [+66.9, +106.6 at +1] steerable, expected; descr +52.6% [+48.0, +74.2 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 15, category: moral -17.7% [-22.1, -10.6 at +1] steerable, reversed; norm -13.2% [-15.4, -10.1 at +1] steerable, reversed; descr -8.2% [-9.4, -4.0 at +1] (of the gap per step) -> normative-shared
  * layer 23, stance: moral +93.6% [+95.7, +168.6 at +1] steerable, expected; norm +90.6% [+81.1, +137.0 at +1] steerable, expected; descr +81.3% [+78.9, +129.5 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 23, category: moral -15.9% [-21.4, -11.4 at +1] steerable, reversed; norm -12.5% [-16.3, -10.3 at +1] steerable, reversed; descr -10.2% [-13.9, -6.6 at +1] steerable, reversed (of the gap per step) -> SHARED
* C: cosine(moral stance, norm stance) by layer L7: 0.75; L15: 0.73; L23: 0.68
  * layer 7, stance: moral +0.1% [+0.0, +0.1 at +1] steerable, expected; norm -0.0% [-0.0, +0.0 at +1]; descr -0.0% [-0.0, -0.0 at +1] steerable, reversed (in moral-word probability per step) -> not shared
  * layer 7, category: moral +0.1% [-0.0, +0.1 at +1]; norm +0.3% [+0.2, +0.3 at +1] steerable, expected; descr +0.0% [+0.0, +0.0 at +1] steerable, expected (in moral-word probability per step) -> not shared
  * layer 15, stance: moral -2.4% [-3.1, -2.0 at +1] steerable, reversed; norm -2.0% [-2.6, -1.4 at +1] steerable, reversed; descr -0.4% [-0.5, -0.2 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 15, category: moral +11.6% [+6.4, +10.0 at +1] steerable, expected; norm +12.4% [+15.7, +21.4 at +1] steerable, expected; descr +2.7% [+3.0, +6.6 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 23, stance: moral -4.2% [-5.8, -3.7 at +1] steerable, reversed; norm -4.7% [-5.3, -3.1 at +1] steerable, reversed; descr -1.1% [-1.0, -0.3 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 23, category: moral +28.0% [+8.5, +14.2 at +1] steerable, expected; norm +35.2% [+56.7, +64.4 at +1] steerable, expected; descr +30.3% [+53.2, +66.3 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Llama-3.1-8B-Instruct

* A1: cosine(moral stance, norm stance) by layer L7: 0.74; L15: 0.79; L23: 0.93
  * layer 7, stance: moral +0.5% [+0.3, +0.9 at +1]; norm +1.8% [+1.3, +2.7 at +1]; descr +2.1% [+1.6, +2.6 at +1] (of the gap per step) -> not shared
  * layer 7, category: moral +1.1% [+0.0, +2.1 at +1]; norm +10.4% [+6.8, +16.2 at +1] steerable, expected; descr +3.3% [+2.0, +7.7 at +1] (of the gap per step) -> not shared
  * layer 15, stance: moral +25.5% [+20.8, +33.4 at +1] steerable, expected; norm +43.7% [+28.2, +45.3 at +1] steerable, expected; descr +37.5% [+25.6, +34.3 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 15, category: moral +1.8% [-3.7, +3.4 at +1]; norm +18.5% [+9.5, +30.9 at +1] steerable, expected; descr +14.2% [+7.6, +22.3 at +1] steerable, expected (of the gap per step) -> not shared
  * layer 23, stance: moral +67.4% [+49.6, +68.9 at +1] steerable, expected; norm +104.8% [+74.3, +116.8 at +1] steerable, expected; descr +104.6% [+92.3, +124.7 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 23, category: moral +0.4% [-5.2, +3.0 at +1]; norm +4.4% [-7.5, +12.2 at +1]; descr +9.5% [+0.0, +15.8 at +1] (of the gap per step) -> not shared
* B: cosine(moral stance, norm stance) by layer L7: 0.70; L15: 0.76; L23: 0.83
  * layer 7, stance: moral +12.4% [+5.1, +19.7 at +1] steerable, expected; norm +4.2% [+2.7, +5.9 at +1]; descr +1.6% [+0.7, +2.6 at +1] (of the gap per step) -> not shared
  * layer 7, category: moral -1.9% [-5.0, +1.2 at +1]; norm -2.7% [-2.9, -1.0 at +1]; descr -1.8% [-1.3, +0.6 at +1] (of the gap per step) -> not shared
  * layer 15, stance: moral +98.7% [+68.5, +156.3 at +1] steerable, expected; norm +65.5% [+56.3, +78.9 at +1] steerable, expected; descr +48.9% [+36.9, +57.1 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 15, category: moral -17.4% [-31.4, -7.3 at +1] steerable, reversed; norm -9.6% [-12.5, -6.9 at +1]; descr -5.3% [-8.0, -2.7 at +1] (of the gap per step) -> not shared
  * layer 23, stance: moral +111.0% [+76.4, +167.1 at +1] steerable, expected; norm +74.5% [+64.3, +89.3 at +1] steerable, expected; descr +70.7% [+64.0, +98.1 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 23, category: moral -14.1% [-27.2, -8.7 at +1] steerable, reversed; norm -7.5% [-11.9, -7.0 at +1]; descr -5.5% [-10.3, -3.8 at +1] (of the gap per step) -> not shared
* C: cosine(moral stance, norm stance) by layer L7: 0.79; L15: 0.75; L23: 0.65
  * layer 7, stance: moral +0.0% [-0.0, +0.1 at +1]; norm -0.1% [-0.1, -0.0 at +1] steerable, reversed; descr -0.0% [-0.0, +0.0 at +1] (in moral-word probability per step) -> not shared
  * layer 7, category: moral +0.2% [+0.0, +0.3 at +1] steerable, expected; norm +0.3% [+0.2, +0.4 at +1] steerable, expected; descr +0.1% [+0.0, +0.1 at +1] (in moral-word probability per step) -> normative-shared
  * layer 15, stance: moral -2.0% [-3.0, -1.7 at +1] steerable, reversed; norm -1.8% [-2.7, -1.2 at +1] steerable, reversed; descr -0.3% [-0.5, -0.1 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 15, category: moral +11.3% [+5.5, +9.3 at +1] steerable, expected; norm +11.3% [+14.2, +20.0 at +1] steerable, expected; descr +1.4% [+1.0, +4.0 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 23, stance: moral -4.3% [-6.5, -4.0 at +1] steerable, reversed; norm -5.1% [-5.4, -3.0 at +1] steerable, reversed; descr -0.8% [-0.9, -0.1 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 23, category: moral +28.4% [+8.3, +14.1 at +1] steerable, expected; norm +34.7% [+57.1, +65.0 at +1] steerable, expected; descr +19.4% [+31.0, +45.1 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Llama-3.2-1B

* A1: cosine(moral stance, norm stance) by layer L3: 0.55; L7: 0.78; L11: 0.92
  * layer 3, stance: moral +0.2% [-0.3, +0.6 at +1]; norm +0.6% [+0.0, +1.4 at +1]; descr +0.6% [-0.0, +1.5 at +1] (of the gap per step) -> not shared
  * layer 3, category: moral +0.2% [-3.2, +2.0 at +1]; norm +11.8% [+7.4, +16.8 at +1] steerable, expected; descr +2.5% [+1.1, +10.5 at +1] (of the gap per step) -> not shared
  * layer 7, stance: moral +2.9% [+1.3, +5.1 at +1]; norm +0.6% [-1.4, +1.9 at +1]; descr +6.4% [+3.6, +8.1 at +1] (of the gap per step) -> not shared
  * layer 7, category: moral +20.0% [+11.0, +24.4 at +1] steerable, expected; norm +44.9% [+30.0, +55.0 at +1] steerable, expected; descr +20.9% [+13.6, +33.0 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 11, stance: moral +124.2% [+101.9, +176.1 at +1] steerable, expected; norm +123.7% [+96.1, +163.9 at +1] steerable, expected; descr +89.4% [+63.8, +120.4 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 11, category: moral -6.8% [-11.8, -4.1 at +1]; norm -0.8% [-8.9, +6.3 at +1]; descr +20.6% [+9.8, +35.3 at +1] steerable, expected (of the gap per step) -> not shared
* B: cosine(moral stance, norm stance) by layer L3: 0.47; L7: 0.79; L11: 0.87
  * layer 3, stance: moral +2.9% [+2.0, +4.2 at +1]; norm +3.0% [+2.3, +3.8 at +1]; descr +0.0% [-0.6, +0.7 at +1] (of the gap per step) -> not shared
  * layer 3, category: moral -2.2% [-3.9, -0.1 at +1]; norm -1.1% [-2.5, +1.4 at +1]; descr -1.1% [-2.1, -0.1 at +1] (of the gap per step) -> not shared
  * layer 7, stance: moral +94.6% [+62.5, +115.9 at +1] steerable, expected; norm +80.4% [+57.6, +84.6 at +1] steerable, expected; descr +22.0% [+14.3, +25.7 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 7, category: moral -33.6% [-50.4, -23.7 at +1] steerable, reversed; norm -16.7% [-26.1, -10.0 at +1] steerable, reversed; descr -0.6% [-7.1, +4.4 at +1] (of the gap per step) -> normative-shared
  * layer 11, stance: moral +151.0% [+95.3, +175.2 at +1] steerable, expected; norm +152.4% [+102.6, +156.2 at +1] steerable, expected; descr +96.3% [+65.1, +102.9 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 11, category: moral -44.8% [-72.7, -34.1 at +1] steerable, reversed; norm -19.7% [-43.1, -17.9 at +1] steerable, reversed; descr -20.4% [-32.5, -15.2 at +1] steerable, reversed (of the gap per step) -> SHARED
* C: cosine(moral stance, norm stance) by layer L3: 0.47; L7: 0.84; L11: 0.69
  * layer 3, stance: moral -0.1% [-0.1, -0.0 at +1] steerable, reversed; norm -0.0% [-0.0, -0.0 at +1] steerable, reversed; descr -0.0% [-0.0, -0.0 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 3, category: moral +0.1% [+0.1, +0.1 at +1] steerable, expected; norm +0.1% [+0.0, +0.1 at +1] steerable, expected; descr -0.0% [-0.0, +0.0 at +1] (in moral-word probability per step) -> normative-shared
  * layer 7, stance: moral -0.4% [-0.7, -0.2 at +1] steerable, reversed; norm -0.1% [-0.2, +0.0 at +1]; descr -0.0% [-0.1, +0.0 at +1] (in moral-word probability per step) -> not shared
  * layer 7, category: moral +2.2% [+1.2, +2.1 at +1] steerable, expected; norm +1.3% [+1.0, +1.8 at +1] steerable, expected; descr +0.5% [+0.4, +0.9 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 11, stance: moral -1.7% [-3.5, -1.3 at +1] steerable, reversed; norm -0.8% [-1.4, -0.3 at +1] steerable, reversed; descr -0.8% [-1.2, -0.5 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 11, category: moral +32.8% [+17.2, +23.5 at +1] steerable, expected; norm +21.4% [+31.5, +39.2 at +1] steerable, expected; descr +24.0% [+38.0, +52.3 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Llama-3.2-1B-Instruct

* A1: cosine(moral stance, norm stance) by layer L3: 0.60; L7: 0.77; L11: 0.86
  * layer 3, stance: moral +1.1% [+0.6, +1.5 at +1]; norm +1.7% [+1.1, +2.2 at +1]; descr +1.7% [+0.8, +2.8 at +1] (of the gap per step) -> not shared
  * layer 3, category: moral -3.1% [-4.3, -0.9 at +1]; norm -3.3% [-3.7, -0.1 at +1]; descr -5.6% [-6.3, -1.3 at +1] (of the gap per step) -> not shared
  * layer 7, stance: moral +8.0% [+6.0, +10.4 at +1]; norm +7.7% [+5.2, +10.2 at +1]; descr +15.3% [+9.2, +21.9 at +1] steerable, expected (of the gap per step) -> not shared
  * layer 7, category: moral -19.5% [-30.7, -8.8 at +1] steerable, reversed; norm -1.2% [-6.7, +3.8 at +1]; descr -29.5% [-58.7, -15.3 at +1] steerable, reversed (of the gap per step) -> not shared
  * layer 11, stance: moral +64.1% [+63.0, +105.7 at +1] steerable, expected; norm +120.4% [+109.6, +161.7 at +1] steerable, expected; descr +109.3% [+71.7, +184.6 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 11, category: moral -61.0% [-67.6, -41.6 at +1] steerable, reversed; norm -95.0% [-123.6, -84.6 at +1] steerable, reversed; descr -84.1% [-154.2, -60.7 at +1] steerable, reversed (of the gap per step) -> SHARED
* B: cosine(moral stance, norm stance) by layer L3: 0.49; L7: 0.83; L11: 0.84
  * layer 3, stance: moral +2.4% [+1.7, +3.7 at +1]; norm +3.4% [+2.4, +4.8 at +1]; descr +1.8% [+0.6, +4.1 at +1] (of the gap per step) -> not shared
  * layer 3, category: moral -6.1% [-8.7, -3.6 at +1]; norm -8.1% [-12.8, -5.9 at +1]; descr -0.6% [-2.7, +0.4 at +1] (of the gap per step) -> not shared
  * layer 7, stance: moral +56.1% [+42.8, +90.4 at +1] steerable, expected; norm +81.6% [+53.9, +95.3 at +1] steerable, expected; descr +22.9% [+12.9, +32.5 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 7, category: moral -26.8% [-44.4, -22.3 at +1] steerable, reversed; norm -30.3% [-38.3, -18.0 at +1] steerable, reversed; descr +3.1% [-8.0, +20.4 at +1] (of the gap per step) -> normative-shared
  * layer 11, stance: moral +95.7% [+80.8, +150.2 at +1] steerable, expected; norm +159.4% [+92.7, +170.3 at +1] steerable, expected; descr +101.0% [+57.5, +117.8 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 11, category: moral -32.6% [-42.5, -18.8 at +1] steerable, reversed; norm -35.8% [-78.6, -39.9 at +1] steerable, reversed; descr -31.5% [-67.8, -24.9 at +1] steerable, reversed (of the gap per step) -> SHARED
* C: cosine(moral stance, norm stance) by layer L3: 0.64; L7: 0.84; L11: 0.68
  * layer 3, stance: moral +0.1% [+0.0, +0.1 at +1] steerable, expected; norm +0.0% [-0.0, +0.0 at +1]; descr +0.1% [+0.0, +0.1 at +1] steerable, expected (in moral-word probability per step) -> not shared
  * layer 3, category: moral +0.1% [+0.0, +0.1 at +1] steerable, expected; norm +0.2% [+0.1, +0.2 at +1] steerable, expected; descr +0.2% [+0.1, +0.3 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 7, stance: moral -0.6% [-0.9, -0.4 at +1] steerable, reversed; norm -0.6% [-1.0, -0.4 at +1] steerable, reversed; descr -0.5% [-0.8, -0.3 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 7, category: moral +1.4% [+0.2, +1.0 at +1] steerable, expected; norm +2.9% [+2.3, +3.7 at +1] steerable, expected; descr +2.4% [+2.0, +3.8 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 11, stance: moral -3.3% [-5.0, -2.8 at +1] steerable, reversed; norm -3.3% [-4.0, -2.3 at +1] steerable, reversed; descr -4.4% [-4.7, -2.6 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 11, category: moral +24.8% [+9.5, +15.2 at +1] steerable, expected; norm +29.7% [+42.4, +51.3 at +1] steerable, expected; descr +30.0% [+43.8, +59.7 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Llama-3.2-3B

* A1: cosine(moral stance, norm stance) by layer L6: 0.61; L13: 0.79; L20: 0.92
  * layer 6, stance: moral -0.3% [-0.8, +0.1 at +1]; norm -1.1% [-2.0, -0.4 at +1]; descr -1.7% [-2.6, -0.9 at +1] (of the gap per step) -> not shared
  * layer 6, category: moral +2.5% [+0.1, +3.0 at +1]; norm +9.2% [+5.9, +12.4 at +1]; descr +3.5% [+1.7, +6.6 at +1] (of the gap per step) -> not shared
  * layer 13, stance: moral +24.1% [+19.2, +34.5 at +1] steerable, expected; norm +46.5% [+34.5, +64.5 at +1] steerable, expected; descr +40.0% [+29.8, +56.0 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 13, category: moral -0.5% [-6.6, +0.2 at +1]; norm +17.1% [+7.6, +19.1 at +1] steerable, expected; descr +6.2% [-2.0, +6.7 at +1] (of the gap per step) -> not shared
  * layer 20, stance: moral +76.6% [+66.2, +143.7 at +1] steerable, expected; norm +126.1% [+100.7, +186.9 at +1] steerable, expected; descr +102.5% [+88.0, +154.6 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 20, category: moral -12.5% [-18.4, -8.0 at +1] steerable, reversed; norm -18.7% [-29.4, -13.5 at +1] steerable, reversed; descr -16.5% [-26.7, -13.3 at +1] steerable, reversed (of the gap per step) -> SHARED
* B: cosine(moral stance, norm stance) by layer L6: 0.53; L13: 0.76; L20: 0.88
  * layer 6, stance: moral +5.4% [+3.4, +8.4 at +1]; norm +6.2% [+4.7, +8.0 at +1]; descr +3.0% [+1.9, +3.7 at +1] (of the gap per step) -> not shared
  * layer 6, category: moral +0.4% [-0.7, +2.5 at +1]; norm -5.2% [-7.0, -2.6 at +1]; descr -3.3% [-4.5, -1.9 at +1] (of the gap per step) -> not shared
  * layer 13, stance: moral +84.8% [+79.8, +165.9 at +1] steerable, expected; norm +94.9% [+69.8, +114.4 at +1] steerable, expected; descr +62.7% [+48.0, +72.2 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 13, category: moral -30.2% [-28.6, -13.4 at +1] steerable, reversed; norm -44.5% [-55.3, -34.7 at +1] steerable, reversed; descr -30.7% [-40.0, -23.9 at +1] steerable, reversed (of the gap per step) -> SHARED
  * layer 20, stance: moral +98.9% [+103.6, +222.1 at +1] steerable, expected; norm +123.7% [+89.5, +146.8 at +1] steerable, expected; descr +104.1% [+82.0, +125.0 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 20, category: moral -27.1% [-26.8, -7.2 at +1] steerable, reversed; norm -51.3% [-70.1, -41.2 at +1] steerable, reversed; descr -42.6% [-54.9, -31.9 at +1] steerable, reversed (of the gap per step) -> SHARED
* C: cosine(moral stance, norm stance) by layer L6: 0.64; L13: 0.77; L20: 0.71
  * layer 6, stance: moral +0.0% [+0.0, +0.1 at +1] steerable, expected; norm -0.0% [-0.0, +0.0 at +1]; descr -0.0% [-0.0, -0.0 at +1] steerable, reversed (in moral-word probability per step) -> not shared
  * layer 6, category: moral +0.0% [-0.0, +0.1 at +1]; norm +0.1% [+0.0, +0.2 at +1] steerable, expected; descr -0.1% [-0.1, -0.0 at +1] (in moral-word probability per step) -> not shared
  * layer 13, stance: moral -0.3% [-0.7, +0.1 at +1]; norm -0.9% [-1.7, -0.4 at +1] steerable, reversed; descr -0.0% [-0.3, +0.1 at +1] (in moral-word probability per step) -> not shared
  * layer 13, category: moral +6.6% [+4.4, +7.0 at +1] steerable, expected; norm +6.5% [+6.9, +9.5 at +1] steerable, expected; descr +2.9% [+2.8, +5.2 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 20, stance: moral -1.4% [-3.0, -1.4 at +1]; norm -1.7% [-3.1, -1.2 at +1] steerable, reversed; descr -1.1% [-1.6, -0.9 at +1] steerable, reversed (in moral-word probability per step) -> not shared
  * layer 20, category: moral +27.3% [+7.8, +13.2 at +1] steerable, expected; norm +34.8% [+52.8, +60.0 at +1] steerable, expected; descr +34.0% [+56.5, +68.3 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Llama-3.2-3B-Instruct

* A1: cosine(moral stance, norm stance) by layer L6: 0.55; L13: 0.79; L20: 0.94
  * layer 6, stance: moral +0.3% [-0.0, +0.5 at +1]; norm +0.7% [+0.2, +0.9 at +1]; descr +0.8% [+0.6, +1.0 at +1] (of the gap per step) -> not shared
  * layer 6, category: moral +0.8% [-0.9, +3.0 at +1]; norm +5.2% [+2.9, +7.1 at +1]; descr +2.4% [+1.3, +5.0 at +1] (of the gap per step) -> not shared
  * layer 13, stance: moral +35.1% [+15.7, +73.8 at +1] steerable, expected; norm +40.0% [+26.7, +52.7 at +1] steerable, expected; descr +33.6% [+22.5, +42.7 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 13, category: moral -3.8% [-12.2, +1.1 at +1]; norm +6.6% [-2.6, +8.4 at +1]; descr +0.7% [-3.3, +0.1 at +1] (of the gap per step) -> not shared
  * layer 20, stance: moral +122.6% [+61.2, +282.1 at +1] steerable, expected; norm +122.6% [+79.6, +210.3 at +1] steerable, expected; descr +83.9% [+73.7, +126.5 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 20, category: moral -23.6% [-33.4, -11.0 at +1] steerable, reversed; norm -26.5% [-39.1, -21.5 at +1] steerable, reversed; descr -23.5% [-37.4, -21.3 at +1] steerable, reversed (of the gap per step) -> SHARED
* B: cosine(moral stance, norm stance) by layer L6: 0.57; L13: 0.77; L20: 0.84
  * layer 6, stance: moral +4.8% [+2.3, +6.6 at +1]; norm +5.8% [+4.2, +8.4 at +1]; descr +2.2% [+1.3, +3.0 at +1] (of the gap per step) -> not shared
  * layer 6, category: moral -0.1% [-0.9, +3.1 at +1]; norm -2.4% [-3.7, -0.4 at +1]; descr -1.3% [-2.5, -0.6 at +1] (of the gap per step) -> not shared
  * layer 13, stance: moral +63.7% [+44.3, +108.9 at +1] steerable, expected; norm +82.6% [+62.7, +126.8 at +1] steerable, expected; descr +45.5% [+32.0, +71.1 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 13, category: moral -10.3% [-17.2, -3.8 at +1] steerable, reversed; norm -22.7% [-32.4, -15.2 at +1] steerable, reversed; descr -12.2% [-17.0, -4.3 at +1] steerable, reversed (of the gap per step) -> SHARED
  * layer 20, stance: moral +90.7% [+66.1, +199.8 at +1] steerable, expected; norm +107.7% [+82.0, +166.4 at +1] steerable, expected; descr +75.4% [+61.6, +123.6 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 20, category: moral -11.3% [-18.1, +3.6 at +1]; norm -24.7% [-36.1, -19.3 at +1] steerable, reversed; descr -16.6% [-21.9, -10.3 at +1] steerable, reversed (of the gap per step) -> not shared
* C: cosine(moral stance, norm stance) by layer L6: 0.66; L13: 0.82; L20: 0.76
  * layer 6, stance: moral -0.0% [-0.1, +0.0 at +1]; norm -0.0% [-0.1, -0.0 at +1] steerable, reversed; descr +0.0% [-0.0, +0.0 at +1] (in moral-word probability per step) -> not shared
  * layer 6, category: moral +0.1% [+0.1, +0.2 at +1] steerable, expected; norm +0.2% [+0.1, +0.3 at +1] steerable, expected; descr -0.1% [-0.2, -0.0 at +1] (in moral-word probability per step) -> normative-shared
  * layer 13, stance: moral +0.4% [+0.4, +1.6 at +1]; norm +0.3% [-0.2, +1.2 at +1]; descr +0.9% [+0.3, +2.1 at +1] steerable, expected (in moral-word probability per step) -> not shared
  * layer 13, category: moral +8.3% [+5.8, +9.2 at +1] steerable, expected; norm +6.2% [+6.8, +9.9 at +1] steerable, expected; descr +2.4% [+2.3, +4.5 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 20, stance: moral -0.4% [-2.0, -0.4 at +1]; norm -0.1% [-1.3, +0.8 at +1]; descr +0.2% [-0.3, +0.8 at +1] (in moral-word probability per step) -> not shared
  * layer 20, category: moral +28.4% [+9.4, +15.3 at +1] steerable, expected; norm +32.0% [+50.8, +58.3 at +1] steerable, expected; descr +27.7% [+45.3, +57.2 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Qwen2.5-14B

* A1: cosine(moral stance, norm stance) by layer L11: 0.53; L23: 0.55; L35: 0.87
  * layer 11, stance: moral -0.0% [-0.1, +0.1 at +1]; norm +0.1% [-0.0, +0.2 at +1]; descr +0.5% [+0.2, +1.0 at +1] (of the gap per step) -> not shared
  * layer 11, category: moral -0.5% [-0.9, -0.2 at +1]; norm -0.3% [-1.0, +0.1 at +1]; descr -0.5% [-2.6, +5.2 at +1] (of the gap per step) -> not shared
  * layer 23, stance: moral +1.6% [+1.0, +2.2 at +1]; norm +4.2% [+3.2, +5.0 at +1]; descr +8.4% [+6.9, +10.0 at +1] (of the gap per step) -> not shared
  * layer 23, category: moral +1.1% [-0.2, +1.6 at +1]; norm +3.9% [+3.8, +13.7 at +1]; descr +2.6% [-4.7, +25.3 at +1] (of the gap per step) -> not shared
  * layer 35, stance: moral +47.1% [+35.4, +86.5 at +1] steerable, expected; norm +77.9% [+43.6, +62.7 at +1] steerable, expected; descr +144.1% [+33.1, +48.2 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 35, category: moral -3.6% [-8.1, -2.2 at +1]; norm -6.0% [-16.9, -2.5 at +1]; descr +12.1% [-24.7, +43.3 at +1] (of the gap per step) -> not shared
* B: cosine(moral stance, norm stance) by layer L11: 0.44; L23: 0.67; L35: 0.78
  * layer 11, stance: moral +0.3% [+0.2, +0.4 at +1]; norm +0.7% [+0.5, +1.3 at +1]; descr +0.1% [-0.1, +0.3 at +1] (of the gap per step) -> not shared
  * layer 11, category: moral -0.5% [-0.9, -0.3 at +1]; norm -0.6% [-1.5, +0.0 at +1]; descr -0.3% [-0.4, +0.1 at +1] (of the gap per step) -> not shared
  * layer 23, stance: moral +8.7% [+5.7, +12.0 at +1]; norm +24.4% [+13.9, +28.3 at +1] steerable, expected; descr +8.1% [+4.4, +15.2 at +1] (of the gap per step) -> not shared
  * layer 23, category: moral -3.3% [-4.3, -1.7 at +1]; norm -5.3% [-7.0, +0.2 at +1]; descr -1.9% [-3.9, -0.3 at +1] (of the gap per step) -> not shared
  * layer 35, stance: moral +66.4% [+62.8, +107.2 at +1] steerable, expected; norm +127.7% [+61.2, +94.9 at +1] steerable, expected; descr +74.3% [+51.9, +115.6 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 35, category: moral -8.3% [-10.7, -5.1 at +1]; norm -10.1% [-17.3, -3.4 at +1] steerable, reversed; descr -13.3% [-25.6, -6.0 at +1] steerable, reversed (of the gap per step) -> not shared
* C: cosine(moral stance, norm stance) by layer L11: 0.57; L23: 0.75; L35: 0.74
  * layer 11, stance: moral +0.0% [+0.0, +0.0 at +1] steerable, expected; norm -0.0% [-0.0, -0.0 at +1]; descr +0.0% [+0.0, +0.0 at +1] steerable, expected (in moral-word probability per step) -> not shared
  * layer 11, category: moral +0.0% [-0.0, +0.1 at +1]; norm +0.0% [+0.0, +0.1 at +1] steerable, expected; descr -0.0% [-0.0, +0.0 at +1] (in moral-word probability per step) -> not shared
  * layer 23, stance: moral +0.1% [-0.2, +0.3 at +1]; norm -0.2% [-0.3, -0.0 at +1] steerable, reversed; descr +0.0% [-0.0, +0.1 at +1] (in moral-word probability per step) -> not shared
  * layer 23, category: moral +3.3% [+2.8, +4.1 at +1] steerable, expected; norm +1.3% [+1.2, +2.1 at +1] steerable, expected; descr +0.3% [+0.2, +0.7 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 35, stance: moral -4.1% [-7.2, -4.7 at +1] steerable, reversed; norm -2.1% [-2.5, -1.4 at +1] steerable, reversed; descr -0.6% [-0.8, -0.3 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 35, category: moral +29.6% [+14.1, +20.1 at +1] steerable, expected; norm +25.2% [+42.3, +50.0 at +1] steerable, expected; descr +16.9% [+26.2, +37.8 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Qwen2.5-14B-Instruct

* A1: cosine(moral stance, norm stance) by layer L11: 0.48; L23: 0.62; L35: 0.86
  * layer 11, stance: moral -0.1% [-0.1, -0.0 at +1]; norm +0.3% [+0.0, +0.5 at +1]; descr -0.0% [-0.4, +0.6 at +1] (of the gap per step) -> not shared
  * layer 11, category: moral -0.3% [-0.8, +0.1 at +1]; norm -1.5% [-3.2, -0.6 at +1]; descr -18.0% [-60.2, -3.6 at +1] steerable, reversed (of the gap per step) -> not shared
  * layer 23, stance: moral +1.0% [+0.3, +1.4 at +1]; norm +8.3% [+5.1, +9.0 at +1]; descr +14.3% [+8.3, +15.8 at +1] steerable, expected (of the gap per step) -> not shared
  * layer 23, category: moral +3.0% [+1.8, +4.0 at +1]; norm -7.7% [-16.6, -0.8 at +1]; descr -46.8% [-127.3, -25.0 at +1] steerable, reversed (of the gap per step) -> not shared
  * layer 35, stance: moral +54.3% [+30.4, +129.4 at +1] steerable, expected; norm +89.9% [+39.3, +62.7 at +1] steerable, expected; descr +241.1% [+39.7, +53.0 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 35, category: moral -4.1% [-7.1, -0.6 at +1]; norm -26.2% [-60.4, -15.3 at +1] steerable, reversed; descr -127.7% [-378.4, -105.2 at +1] steerable, reversed (of the gap per step) -> not shared
* B: cosine(moral stance, norm stance) by layer L11: 0.43; L23: 0.69; L35: 0.72
  * layer 11, stance: moral +0.1% [-0.0, +0.3 at +1]; norm +0.3% [+0.2, +0.5 at +1]; descr +0.3% [-0.1, +0.9 at +1] (of the gap per step) -> not shared
  * layer 11, category: moral -0.3% [-0.7, -0.1 at +1]; norm -0.2% [-0.8, +0.2 at +1]; descr -0.7% [-2.8, +0.1 at +1] (of the gap per step) -> not shared
  * layer 23, stance: moral +6.4% [+3.2, +8.1 at +1]; norm +14.9% [+10.3, +21.1 at +1] steerable, expected; descr +7.9% [+2.9, +18.6 at +1] (of the gap per step) -> not shared
  * layer 23, category: moral -1.0% [-1.6, +0.8 at +1]; norm -3.4% [-5.9, -2.3 at +1]; descr -0.7% [-4.9, +1.1 at +1] (of the gap per step) -> not shared
  * layer 35, stance: moral +59.7% [+59.1, +101.3 at +1] steerable, expected; norm +81.2% [+51.9, +80.8 at +1] steerable, expected; descr +74.7% [+52.3, +139.7 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 35, category: moral -4.9% [-6.1, -2.0 at +1]; norm -9.1% [-14.6, -6.0 at +1]; descr -14.0% [-27.3, -4.1 at +1] steerable, reversed (of the gap per step) -> not shared
* C: cosine(moral stance, norm stance) by layer L11: 0.56; L23: 0.76; L35: 0.73
  * layer 11, stance: moral +0.0% [-0.0, +0.0 at +1]; norm +0.0% [-0.0, +0.0 at +1]; descr +0.0% [-0.0, +0.0 at +1] (in moral-word probability per step) -> not shared
  * layer 11, category: moral +0.0% [-0.0, +0.1 at +1]; norm +0.0% [+0.0, +0.0 at +1] steerable, expected; descr -0.0% [-0.0, -0.0 at +1] (in moral-word probability per step) -> not shared
  * layer 23, stance: moral -0.7% [-1.1, -0.5 at +1] steerable, reversed; norm -0.3% [-0.5, -0.1 at +1] steerable, reversed; descr +0.0% [-0.0, +0.1 at +1] (in moral-word probability per step) -> normative-shared
  * layer 23, category: moral +3.3% [+2.6, +4.2 at +1] steerable, expected; norm +1.1% [+0.9, +1.9 at +1] steerable, expected; descr +0.1% [+0.1, +0.3 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 35, stance: moral -7.8% [-10.9, -7.4 at +1] steerable, reversed; norm -2.7% [-2.8, -1.3 at +1] steerable, reversed; descr -0.5% [-0.6, -0.1 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 35, category: moral +31.1% [+14.0, +21.2 at +1] steerable, expected; norm +26.2% [+44.3, +53.6 at +1] steerable, expected; descr +18.1% [+27.7, +42.4 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Qwen2.5-3B

* A1: cosine(moral stance, norm stance) by layer L8: 0.35; L17: 0.70; L26: 0.84
  * layer 8, stance: moral +0.2% [+0.1, +0.4 at +1]; norm -0.1% [-0.3, +0.2 at +1]; descr +0.3% [+0.1, +0.5 at +1] (of the gap per step) -> not shared
  * layer 8, category: moral -3.7% [-4.8, -2.0 at +1]; norm -7.3% [-8.3, -4.6 at +1]; descr -3.4% [-5.1, -2.2 at +1] (of the gap per step) -> not shared
  * layer 17, stance: moral +4.7% [+3.3, +6.2 at +1]; norm +5.3% [+3.8, +6.3 at +1]; descr +5.0% [+3.8, +5.9 at +1] (of the gap per step) -> not shared
  * layer 17, category: moral -4.2% [-8.1, +1.0 at +1]; norm +0.2% [+1.0, +11.0 at +1]; descr +8.1% [+5.9, +16.8 at +1] (of the gap per step) -> not shared
  * layer 26, stance: moral +74.7% [+64.2, +126.7 at +1] steerable, expected; norm +92.8% [+91.4, +136.8 at +1] steerable, expected; descr +96.4% [+79.9, +134.1 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 26, category: moral -4.5% [-12.9, +3.6 at +1]; norm +0.9% [+0.3, +8.7 at +1]; descr +6.1% [+2.9, +9.9 at +1] (of the gap per step) -> not shared
* B: cosine(moral stance, norm stance) by layer L8: 0.21; L17: 0.65; L26: 0.80
  * layer 8, stance: moral +1.1% [+0.7, +1.6 at +1]; norm +0.9% [+0.4, +1.6 at +1]; descr +0.0% [-0.2, +0.2 at +1] (of the gap per step) -> not shared
  * layer 8, category: moral -0.9% [-2.4, +0.1 at +1]; norm -1.2% [-3.1, +0.0 at +1]; descr +0.3% [-0.3, +0.8 at +1] (of the gap per step) -> not shared
  * layer 17, stance: moral +19.6% [+13.5, +27.8 at +1] steerable, expected; norm +17.7% [+12.7, +21.3 at +1] steerable, expected; descr +8.4% [+4.7, +10.5 at +1] (of the gap per step) -> normative-shared
  * layer 17, category: moral -7.3% [-11.2, -5.0 at +1]; norm -7.0% [-14.0, -2.6 at +1]; descr -6.4% [-9.8, -4.2 at +1] (of the gap per step) -> not shared
  * layer 26, stance: moral +96.8% [+90.9, +170.1 at +1] steerable, expected; norm +121.6% [+104.0, +166.6 at +1] steerable, expected; descr +96.6% [+68.6, +137.7 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 26, category: moral -36.6% [-47.3, -25.7 at +1] steerable, reversed; norm -51.2% [-71.8, -41.0 at +1] steerable, reversed; descr -33.7% [-52.1, -24.0 at +1] steerable, reversed (of the gap per step) -> SHARED
* C: cosine(moral stance, norm stance) by layer L8: 0.45; L17: 0.74; L26: 0.80
  * layer 8, stance: moral +0.0% [+0.0, +0.0 at +1] steerable, expected; norm +0.0% [-0.0, +0.0 at +1]; descr -0.0% [-0.0, +0.0 at +1] (in moral-word probability per step) -> not shared
  * layer 8, category: moral +0.0% [+0.0, +0.1 at +1] steerable, expected; norm +0.1% [+0.1, +0.1 at +1] steerable, expected; descr +0.2% [+0.2, +0.3 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 17, stance: moral +0.1% [+0.0, +0.1 at +1] steerable, expected; norm -0.1% [-0.1, -0.0 at +1] steerable, reversed; descr -0.1% [-0.3, -0.0 at +1] steerable, reversed (in moral-word probability per step) -> not shared
  * layer 17, category: moral +0.5% [+0.3, +0.7 at +1] steerable, expected; norm +0.8% [+0.6, +1.1 at +1] steerable, expected; descr +1.2% [+0.9, +1.8 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 26, stance: moral -1.7% [-3.1, -1.3 at +1] steerable, reversed; norm -2.7% [-3.4, -1.9 at +1] steerable, reversed; descr -4.0% [-4.6, -2.4 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 26, category: moral +17.4% [+9.1, +13.3 at +1] steerable, expected; norm +14.1% [+18.2, +24.2 at +1] steerable, expected; descr +19.4% [+26.2, +36.1 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Qwen2.5-3B-Instruct

* A1: cosine(moral stance, norm stance) by layer L8: 0.61; L17: 0.72; L26: 0.90
  * layer 8, stance: moral -0.0% [-0.1, +0.1 at +1]; norm -0.0% [-0.2, +0.0 at +1]; descr +0.1% [-0.0, +0.2 at +1] (of the gap per step) -> not shared
  * layer 8, category: moral -0.8% [-1.6, -0.3 at +1]; norm -0.7% [-1.1, -0.2 at +1]; descr +0.2% [-0.7, +0.9 at +1] (of the gap per step) -> not shared
  * layer 17, stance: moral +0.5% [+0.1, +0.7 at +1]; norm +0.6% [+0.2, +0.9 at +1]; descr +1.9% [+1.2, +2.5 at +1] (of the gap per step) -> not shared
  * layer 17, category: moral -1.7% [-3.6, -0.8 at +1]; norm +4.6% [+3.0, +6.0 at +1]; descr +1.3% [-0.5, +3.7 at +1] (of the gap per step) -> not shared
  * layer 26, stance: moral +48.1% [+39.2, +83.7 at +1] steerable, expected; norm +61.2% [+41.4, +71.8 at +1] steerable, expected; descr +63.9% [+39.3, +78.8 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 26, category: moral -8.5% [-12.9, -5.9 at +1]; norm -3.7% [-6.0, -2.5 at +1]; descr -12.6% [-25.0, -6.8 at +1] steerable, reversed (of the gap per step) -> not shared
* B: cosine(moral stance, norm stance) by layer L8: 0.35; L17: 0.76; L26: 0.84
  * layer 8, stance: moral +0.6% [+0.3, +0.9 at +1]; norm +0.1% [-0.3, +0.5 at +1]; descr +0.1% [-0.2, +0.5 at +1] (of the gap per step) -> not shared
  * layer 8, category: moral +0.6% [+0.0, +1.4 at +1]; norm +0.2% [-0.3, +0.8 at +1]; descr +0.2% [-0.4, +1.0 at +1] (of the gap per step) -> not shared
  * layer 17, stance: moral +18.9% [+9.7, +19.7 at +1] steerable, expected; norm +15.4% [+9.5, +18.5 at +1] steerable, expected; descr +6.3% [+3.0, +7.0 at +1] (of the gap per step) -> normative-shared
  * layer 17, category: moral -0.6% [-3.9, +3.4 at +1]; norm -0.5% [-3.4, +0.5 at +1]; descr -2.8% [-4.7, -0.2 at +1] (of the gap per step) -> not shared
  * layer 26, stance: moral +112.1% [+94.6, +187.9 at +1] steerable, expected; norm +115.0% [+79.3, +158.8 at +1] steerable, expected; descr +74.9% [+54.4, +116.8 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 26, category: moral -14.2% [-19.9, -5.4 at +1] steerable, reversed; norm -19.9% [-31.5, -12.0 at +1] steerable, reversed; descr -14.7% [-28.3, -7.4 at +1] steerable, reversed (of the gap per step) -> SHARED
* C: cosine(moral stance, norm stance) by layer L8: 0.52; L17: 0.79; L26: 0.80
  * layer 8, stance: moral +0.0% [-0.0, +0.0 at +1]; norm +0.0% [-0.0, +0.0 at +1]; descr -0.0% [-0.0, +0.0 at +1] (in moral-word probability per step) -> not shared
  * layer 8, category: moral +0.1% [+0.1, +0.1 at +1] steerable, expected; norm +0.1% [+0.1, +0.2 at +1] steerable, expected; descr +0.1% [+0.1, +0.2 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 17, stance: moral +0.0% [-0.2, +0.2 at +1]; norm -0.1% [-0.3, -0.1 at +1]; descr -0.2% [-0.4, -0.1 at +1] steerable, reversed (in moral-word probability per step) -> not shared
  * layer 17, category: moral +0.5% [+0.2, +0.6 at +1] steerable, expected; norm +0.9% [+0.6, +1.3 at +1] steerable, expected; descr +0.8% [+0.4, +1.5 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 26, stance: moral -2.7% [-3.8, -2.0 at +1] steerable, reversed; norm -2.3% [-3.2, -1.1 at +1] steerable, reversed; descr -1.1% [-1.4, -0.3 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 26, category: moral +17.3% [+7.1, +11.4 at +1] steerable, expected; norm +19.2% [+25.7, +32.9 at +1] steerable, expected; descr +10.8% [+14.4, +22.8 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Qwen2.5-7B

* A1: cosine(moral stance, norm stance) by layer L6: 0.60; L13: 0.73; L20: 0.87
  * layer 6, stance: moral +0.3% [+0.2, +0.5 at +1]; norm +0.6% [+0.4, +0.9 at +1]; descr +0.7% [+0.5, +0.8 at +1] (of the gap per step) -> not shared
  * layer 6, category: moral -0.8% [-1.4, -0.6 at +1]; norm -1.1% [-3.3, -0.5 at +1]; descr +1.3% [+0.3, +1.9 at +1] (of the gap per step) -> not shared
  * layer 13, stance: moral +5.7% [+3.7, +7.8 at +1]; norm +6.6% [+3.8, +12.1 at +1]; descr +4.9% [+4.0, +6.0 at +1] (of the gap per step) -> not shared
  * layer 13, category: moral -2.3% [-4.8, -0.7 at +1]; norm +3.1% [+0.7, +6.0 at +1]; descr +5.3% [+3.2, +7.6 at +1] (of the gap per step) -> not shared
  * layer 20, stance: moral +68.6% [+53.8, +128.7 at +1] steerable, expected; norm +92.1% [+58.2, +147.9 at +1] steerable, expected; descr +77.6% [+57.6, +91.7 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 20, category: moral -5.8% [-9.2, -3.3 at +1]; norm -5.9% [-12.0, -3.3 at +1]; descr +3.6% [-4.1, +4.7 at +1] (of the gap per step) -> not shared
* B: cosine(moral stance, norm stance) by layer L6: 0.43; L13: 0.71; L20: 0.83
  * layer 6, stance: moral +1.0% [+0.4, +1.7 at +1]; norm +0.9% [+0.5, +1.4 at +1]; descr +0.6% [+0.4, +0.9 at +1] (of the gap per step) -> not shared
  * layer 6, category: moral -0.1% [-1.8, +3.1 at +1]; norm -1.7% [-2.8, -1.0 at +1]; descr -0.7% [-1.4, -0.2 at +1] (of the gap per step) -> not shared
  * layer 13, stance: moral +21.4% [+14.6, +36.0 at +1] steerable, expected; norm +21.8% [+13.4, +28.3 at +1] steerable, expected; descr +9.4% [+6.3, +10.4 at +1] (of the gap per step) -> normative-shared
  * layer 13, category: moral -12.6% [-20.7, -5.6 at +1] steerable, reversed; norm -9.1% [-14.6, -6.0 at +1]; descr -6.9% [-10.6, -4.2 at +1] (of the gap per step) -> not shared
  * layer 20, stance: moral +116.9% [+83.4, +276.1 at +1] steerable, expected; norm +104.3% [+62.9, +120.4 at +1] steerable, expected; descr +58.8% [+47.6, +76.9 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 20, category: moral -12.0% [-14.7, -5.1 at +1] steerable, reversed; norm -12.9% [-20.3, -7.1 at +1] steerable, reversed; descr -9.0% [-13.7, -6.0 at +1] (of the gap per step) -> normative-shared
* C: cosine(moral stance, norm stance) by layer L6: 0.62; L13: 0.68; L20: 0.78
  * layer 6, stance: moral +0.0% [-0.0, +0.0 at +1]; norm +0.0% [-0.0, +0.0 at +1]; descr -0.0% [-0.0, +0.0 at +1] (in moral-word probability per step) -> not shared
  * layer 6, category: moral +0.1% [+0.1, +0.2 at +1] steerable, expected; norm +0.1% [+0.1, +0.1 at +1] steerable, expected; descr +0.0% [+0.0, +0.1 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 13, stance: moral -0.6% [-0.9, -0.5 at +1] steerable, reversed; norm -0.4% [-0.5, -0.3 at +1] steerable, reversed; descr -0.1% [-0.2, -0.1 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 13, category: moral +3.1% [+1.8, +3.1 at +1] steerable, expected; norm +2.2% [+1.8, +3.3 at +1] steerable, expected; descr +0.5% [+0.3, +0.8 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 20, stance: moral -2.6% [-3.4, -2.0 at +1] steerable, reversed; norm -1.7% [-2.1, -1.0 at +1] steerable, reversed; descr -0.5% [-0.8, -0.2 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 20, category: moral +15.8% [+7.7, +11.3 at +1] steerable, expected; norm +13.5% [+18.3, +24.9 at +1] steerable, expected; descr +5.7% [+7.2, +12.6 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Qwen2.5-7B-Instruct

* A1: cosine(moral stance, norm stance) by layer L6: 0.55; L13: 0.76; L20: 0.82
  * layer 6, stance: moral +0.1% [+0.0, +0.2 at +1]; norm +1.2% [+0.7, +1.7 at +1]; descr +0.6% [+0.3, +0.8 at +1] (of the gap per step) -> not shared
  * layer 6, category: moral -0.0% [-0.4, +0.4 at +1]; norm -4.5% [-6.8, -3.1 at +1]; descr -3.9% [-5.5, -2.4 at +1] (of the gap per step) -> not shared
  * layer 13, stance: moral +1.8% [+0.6, +3.0 at +1]; norm +3.3% [+1.1, +5.3 at +1]; descr +3.3% [+1.5, +4.3 at +1] (of the gap per step) -> not shared
  * layer 13, category: moral +1.6% [-1.3, +1.8 at +1]; norm +14.7% [+12.4, +24.4 at +1] steerable, expected; descr -3.3% [-4.1, +2.0 at +1] (of the gap per step) -> not shared
  * layer 20, stance: moral +40.0% [+28.7, +75.3 at +1] steerable, expected; norm +94.2% [+75.6, +165.3 at +1] steerable, expected; descr +87.6% [+62.8, +109.5 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 20, category: moral -0.8% [-4.1, +2.4 at +1]; norm -12.2% [-18.9, -5.2 at +1] steerable, reversed; descr -2.2% [-13.6, -1.5 at +1] (of the gap per step) -> not shared
* B: cosine(moral stance, norm stance) by layer L6: 0.35; L13: 0.66; L20: 0.82
  * layer 6, stance: moral +0.2% [-0.8, +1.1 at +1]; norm +0.2% [-0.4, +0.5 at +1]; descr -0.2% [-0.4, -0.0 at +1] (of the gap per step) -> not shared
  * layer 6, category: moral -1.9% [-4.4, +0.4 at +1]; norm -0.6% [-2.0, -0.3 at +1]; descr +0.2% [-0.4, +0.7 at +1] (of the gap per step) -> not shared
  * layer 13, stance: moral +20.8% [+12.5, +37.8 at +1] steerable, expected; norm +24.2% [+11.5, +30.3 at +1] steerable, expected; descr +5.6% [+3.8, +7.4 at +1] (of the gap per step) -> normative-shared
  * layer 13, category: moral -10.7% [-14.2, -3.3 at +1] steerable, reversed; norm -9.2% [-13.6, -5.9 at +1]; descr -3.7% [-4.6, -1.7 at +1] (of the gap per step) -> not shared
  * layer 20, stance: moral +120.4% [+97.1, +302.8 at +1] steerable, expected; norm +131.1% [+71.2, +137.1 at +1] steerable, expected; descr +59.8% [+53.4, +83.3 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 20, category: moral -13.3% [-14.1, -3.8 at +1] steerable, reversed; norm -11.2% [-17.8, -6.0 at +1] steerable, reversed; descr -7.7% [-11.5, -5.7 at +1] (of the gap per step) -> normative-shared
* C: cosine(moral stance, norm stance) by layer L6: 0.64; L13: 0.70; L20: 0.75
  * layer 6, stance: moral +0.0% [-0.0, +0.0 at +1]; norm -0.0% [-0.0, +0.0 at +1]; descr -0.0% [-0.0, -0.0 at +1] steerable, reversed (in moral-word probability per step) -> not shared
  * layer 6, category: moral +0.0% [+0.0, +0.1 at +1]; norm +0.1% [+0.0, +0.1 at +1] steerable, expected; descr +0.0% [+0.0, +0.1 at +1] steerable, expected (in moral-word probability per step) -> not shared
  * layer 13, stance: moral -0.6% [-0.9, -0.4 at +1] steerable, reversed; norm -0.5% [-0.8, -0.4 at +1] steerable, reversed; descr -0.2% [-0.4, -0.1 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 13, category: moral +2.7% [+1.7, +3.0 at +1] steerable, expected; norm +2.0% [+1.5, +3.0 at +1] steerable, expected; descr +0.5% [+0.2, +0.8 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 20, stance: moral -2.7% [-3.3, -2.0 at +1] steerable, reversed; norm -2.4% [-3.0, -1.5 at +1] steerable, reversed; descr -0.9% [-1.4, -0.4 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 20, category: moral +15.7% [+7.3, +11.1 at +1] steerable, expected; norm +15.7% [+21.6, +29.4 at +1] steerable, expected; descr +6.2% [+7.1, +14.4 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## gemma-2b

* A1: cosine(moral stance, norm stance) by layer L3: 0.48; L8: 0.74; L13: 0.93
  * layer 3, stance: moral -1.3% [-2.7, -0.4 at +1]; norm -0.0% [-0.5, +0.4 at +1]; descr -0.7% [-1.1, -0.2 at +1] (of the gap per step) -> not shared
  * layer 3, category: moral +0.2% [-1.3, +1.9 at +1]; norm +2.1% [+1.4, +3.8 at +1]; descr +2.7% [+1.7, +5.9 at +1] (of the gap per step) -> not shared
  * layer 8, stance: moral +7.3% [+4.3, +12.4 at +1]; norm +8.3% [+5.6, +10.0 at +1]; descr +3.3% [+1.6, +5.0 at +1] (of the gap per step) -> not shared
  * layer 8, category: moral +1.0% [-4.3, +0.3 at +1]; norm +9.0% [+4.0, +7.9 at +1]; descr +14.1% [+8.5, +15.6 at +1] steerable, expected (of the gap per step) -> not shared
  * layer 13, stance: moral +119.4% [+99.3, +266.5 at +1] steerable, expected; norm +131.5% [+111.3, +169.6 at +1] steerable, expected; descr +103.9% [+93.3, +175.6 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 13, category: moral -23.8% [-30.9, -14.5 at +1] steerable, reversed; norm -27.6% [-37.1, -22.7 at +1] steerable, reversed; descr -13.9% [-19.9, -11.3 at +1] steerable, reversed (of the gap per step) -> SHARED
* B: cosine(moral stance, norm stance) by layer L3: 0.36; L8: 0.71; L13: 0.85
  * layer 3, stance: moral +1.9% [+1.2, +2.7 at +1]; norm +1.7% [+1.2, +2.6 at +1]; descr +1.7% [+0.7, +3.1 at +1] (of the gap per step) -> not shared
  * layer 3, category: moral +0.6% [-0.6, +2.0 at +1]; norm -0.8% [-1.5, -0.3 at +1]; descr -1.6% [-2.7, +0.4 at +1] (of the gap per step) -> not shared
  * layer 8, stance: moral +34.2% [+27.8, +61.4 at +1] steerable, expected; norm +43.5% [+28.7, +62.8 at +1] steerable, expected; descr +33.7% [+11.6, +53.9 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 8, category: moral +6.2% [-0.1, +20.0 at +1]; norm -0.5% [-4.1, +2.9 at +1]; descr +0.9% [-4.3, +5.4 at +1] (of the gap per step) -> not shared
  * layer 13, stance: moral +95.0% [+98.7, +207.0 at +1] steerable, expected; norm +135.1% [+94.0, +195.9 at +1] steerable, expected; descr +169.1% [+72.7, +304.2 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 13, category: moral -13.2% [-15.9, +4.7 at +1]; norm -36.6% [-53.0, -25.0 at +1] steerable, reversed; descr -50.7% [-96.7, -25.2 at +1] steerable, reversed (of the gap per step) -> not shared
* C: cosine(moral stance, norm stance) by layer L3: 0.40; L8: 0.76; L13: 0.76
  * layer 3, stance: moral -0.0% [-0.1, -0.0 at +1] steerable, reversed; norm -0.0% [-0.0, -0.0 at +1] steerable, reversed; descr +0.0% [+0.0, +0.0 at +1] steerable, expected (in moral-word probability per step) -> normative-shared
  * layer 3, category: moral -0.0% [-0.1, +0.0 at +1]; norm +0.0% [+0.0, +0.1 at +1] steerable, expected; descr -0.0% [-0.1, +0.0 at +1] (in moral-word probability per step) -> not shared
  * layer 8, stance: moral -0.4% [-0.5, -0.3 at +1] steerable, reversed; norm -0.2% [-0.2, -0.1 at +1] steerable, reversed; descr -0.0% [-0.0, +0.0 at +1] (in moral-word probability per step) -> normative-shared
  * layer 8, category: moral +2.1% [+1.6, +2.3 at +1] steerable, expected; norm +1.0% [+0.8, +1.5 at +1] steerable, expected; descr +0.4% [+0.2, +0.9 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 13, stance: moral -6.4% [-7.9, -5.6 at +1] steerable, reversed; norm -2.2% [-2.3, -1.1 at +1] steerable, reversed; descr -1.2% [-1.8, -0.3 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 13, category: moral +33.6% [+19.7, +27.6 at +1] steerable, expected; norm +22.3% [+35.1, +43.7 at +1] steerable, expected; descr +13.4% [+18.8, +30.7 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## gemma-2b-it

* A1: cosine(moral stance, norm stance) by layer L3: 0.47; L8: 0.76; L13: 0.91
  * layer 3, stance: moral +0.1% [+0.0, +0.2 at +1]; norm +0.3% [+0.1, +0.5 at +1]; descr +0.8% [+0.3, +1.2 at +1] (of the gap per step) -> not shared
  * layer 3, category: moral -1.2% [-1.8, -0.6 at +1]; norm -1.8% [-2.6, -1.0 at +1]; descr -2.6% [-4.0, -1.5 at +1] (of the gap per step) -> not shared
  * layer 8, stance: moral +8.7% [+6.4, +12.6 at +1]; norm +16.4% [+11.9, +24.1 at +1] steerable, expected; descr +16.8% [+9.8, +24.8 at +1] steerable, expected (of the gap per step) -> not shared
  * layer 8, category: moral -11.3% [-15.6, -6.0 at +1] steerable, reversed; norm -14.2% [-19.9, -6.4 at +1] steerable, reversed; descr -3.7% [-8.0, +1.3 at +1] (of the gap per step) -> normative-shared
  * layer 13, stance: moral +107.6% [+93.7, +202.6 at +1] steerable, expected; norm +187.0% [+126.6, +299.5 at +1] steerable, expected; descr +156.0% [+98.3, +267.7 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 13, category: moral -45.2% [-52.8, -27.2 at +1] steerable, reversed; norm -76.5% [-99.6, -55.2 at +1] steerable, reversed; descr -53.4% [-102.1, -43.2 at +1] steerable, reversed (of the gap per step) -> SHARED
* B: cosine(moral stance, norm stance) by layer L3: 0.29; L8: 0.69; L13: 0.81
  * layer 3, stance: moral +0.9% [+0.2, +1.6 at +1]; norm +1.1% [+0.5, +1.9 at +1]; descr +0.2% [-0.3, +0.4 at +1] (of the gap per step) -> not shared
  * layer 3, category: moral +3.0% [+1.3, +5.1 at +1]; norm +2.4% [+0.8, +4.1 at +1]; descr -0.3% [-1.6, +1.2 at +1] (of the gap per step) -> not shared
  * layer 8, stance: moral +26.8% [+13.8, +44.7 at +1] steerable, expected; norm +27.5% [+18.4, +37.6 at +1] steerable, expected; descr +11.9% [+5.4, +17.2 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 8, category: moral -4.5% [-22.5, +6.6 at +1]; norm -4.3% [-11.4, -1.1 at +1]; descr -5.1% [-11.4, -1.0 at +1] (of the gap per step) -> not shared
  * layer 13, stance: moral +116.0% [+67.7, +191.8 at +1] steerable, expected; norm +114.8% [+80.7, +147.1 at +1] steerable, expected; descr +100.7% [+59.3, +130.7 at +1] steerable, expected (of the gap per step) -> SHARED
  * layer 13, category: moral -44.3% [-72.0, -20.8 at +1] steerable, reversed; norm -29.5% [-50.8, -25.8 at +1] steerable, reversed; descr -28.7% [-50.2, -19.4 at +1] steerable, reversed (of the gap per step) -> SHARED
* C: cosine(moral stance, norm stance) by layer L3: 0.33; L8: 0.77; L13: 0.72
  * layer 3, stance: moral -0.0% [-0.0, +0.0 at +1]; norm -0.0% [-0.0, +0.0 at +1]; descr -0.0% [-0.1, -0.0 at +1] steerable, reversed (in moral-word probability per step) -> not shared
  * layer 3, category: moral -0.0% [-0.1, +0.0 at +1]; norm +0.1% [+0.0, +0.2 at +1] steerable, expected; descr -0.3% [-0.4, -0.2 at +1] steerable, reversed (in moral-word probability per step) -> not shared
  * layer 8, stance: moral -0.4% [-0.5, -0.1 at +1] steerable, reversed; norm -1.5% [-1.9, -0.9 at +1] steerable, reversed; descr -1.0% [-1.2, -0.3 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 8, category: moral +0.7% [+0.3, +1.0 at +1] steerable, expected; norm +6.6% [+6.0, +8.7 at +1] steerable, expected; descr +5.8% [+4.9, +8.5 at +1] steerable, expected (in moral-word probability per step) -> SHARED
  * layer 13, stance: moral -2.5% [-3.8, -1.7 at +1] steerable, reversed; norm -8.0% [-8.9, -5.8 at +1] steerable, reversed; descr -9.2% [-11.3, -6.8 at +1] steerable, reversed (in moral-word probability per step) -> SHARED
  * layer 13, category: moral +14.7% [+3.0, +7.3 at +1] steerable, expected; norm +38.7% [+43.1, +53.0 at +1] steerable, expected; descr +35.2% [+28.5, +42.6 at +1] steerable, expected (in moral-word probability per step) -> SHARED

## Counts of models (any layer counts once per model and frame)

* frame A1, category, normative: 6 of 14 models (Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, gemma-2b, gemma-2b-it)
* frame A1, category, shared: 6 of 14 models (Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, gemma-2b, gemma-2b-it)
* frame A1, stance, normative: 14 of 14 models (Llama-3.1-8B, Llama-3.1-8B-Instruct, Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B, Qwen2.5-7B-Instruct, gemma-2b, gemma-2b-it)
* frame A1, stance, shared: 14 of 14 models (Llama-3.1-8B, Llama-3.1-8B-Instruct, Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B, Qwen2.5-7B-Instruct, gemma-2b, gemma-2b-it)
* frame B, category, normative: 10 of 14 models (Llama-3.1-8B, Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B, Qwen2.5-7B-Instruct, gemma-2b-it)
* frame B, category, shared: 8 of 14 models (Llama-3.1-8B, Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, gemma-2b-it)
* frame B, stance, normative: 14 of 14 models (Llama-3.1-8B, Llama-3.1-8B-Instruct, Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B, Qwen2.5-7B-Instruct, gemma-2b, gemma-2b-it)
* frame B, stance, shared: 14 of 14 models (Llama-3.1-8B, Llama-3.1-8B-Instruct, Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B, Qwen2.5-7B-Instruct, gemma-2b, gemma-2b-it)
* frame C, category, normative: 14 of 14 models (Llama-3.1-8B, Llama-3.1-8B-Instruct, Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B, Qwen2.5-7B-Instruct, gemma-2b, gemma-2b-it)
* frame C, category, shared: 14 of 14 models (Llama-3.1-8B, Llama-3.1-8B-Instruct, Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B, Qwen2.5-7B-Instruct, gemma-2b, gemma-2b-it)
* frame C, stance, normative: 12 of 14 models (Llama-3.1-8B, Llama-3.1-8B-Instruct, Llama-3.2-1B, Llama-3.2-1B-Instruct, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B, Qwen2.5-7B-Instruct, gemma-2b, gemma-2b-it)
* frame C, stance, shared: 12 of 14 models (Llama-3.1-8B, Llama-3.1-8B-Instruct, Llama-3.2-1B, Llama-3.2-1B-Instruct, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B, Qwen2.5-7B-Instruct, gemma-2b, gemma-2b-it)
