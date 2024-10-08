<!-- Digital version -->
<div style="border: 1px solid black; width: 8.5in; height: 11in; padding: 1in; box-sizing: border-box; position: relative; font-size: 10px;">
<!-- Printable version -->
<!-- <div style="width: 8.5in; height: 11in; padding: 1in; box-sizing: border-box; position: relative; font-size: 10px;"> -->

<h4 style="margin: 0;">Trigonometric Identities</h4>
<!-- The blank rows in each <td> block, and lack of indents inside the table HTML, are so the KaTeX parser doesn't break while parsing formulas inside the $$ signs, as discovered through trial and error. -->
<table style="width: 100%">
<tr>
<td style="vertical-align: top;">

$$ 
\sin^2(x) = 1 - \cos^2(x) \\[0.1cm]
\hspace{1.25cm} = \dfrac{1 - \cos(2x)}{2} \\[0.3cm]
\cos^2(x) = 1 - \sin^2(x) \\[0.1cm]
\hspace{1.25cm} = \dfrac{1 + \cos(2x)}{2} 
$$
</td>
<td style="vertical-align: top;">

$$
\sin(2x) = 2\sin(x)\cos(x) \\[0.1cm]
\hspace{0.85cm} = \dfrac{2\tan(x)}{1 + \tan^2(x)} \\[0.3cm]
\cos(2x) = \cos^2(x) - \sin^2(x) \\[0.1cm]
\hspace{0.55cm} = 1 - 2\sin^2(x) \\[0.1cm]
\hspace{0.55cm} = 2\cos^{2}(x) - 1
$$
</td>
<td style="vertical-align: top;">

$$
\tan^2(x) = \sec^2(x) - 1 \\[0.3cm]
\cot^2(x) = \csc^2(x) - 1 \\[0.3cm]
\sec^2(x) = 1 + \tan^2(x) \\[0.3cm]
\csc^2(x) = 1 + \cot^2(x)
$$
</td>
</tr>
</table>

<h4 style="margin: 0;">Trigonometric Derivatives</h4>
<!-- The blank rows in each <td> block, and lack of indents inside the table HTML, are so the KaTeX parser doesn't break while parsing formulas inside the $$ signs, as discovered through trial and error. -->
<table style="width: 100%; text-align: left;">
<tr>
<td style="vertical-align: top;">

$$
\dfrac{d}{dx} \sin(x) = \cos(x) \\[0.3cm]
\dfrac{d}{dx} \cos(x) = -\sin(x) \\[0.3cm]
\dfrac{d}{dx} \tan(x) = \sec^2(x)
$$
</td>
<td style="vertical-align: top;">

$$
\dfrac{d}{dx} \csc(x) = -\csc(x)\cot(x) \\[0.3cm]
\dfrac{d}{dx} \sec(x) = \sec(x)\tan(x) \\[0.3cm]
\dfrac{d}{dx} \cot(x) = -\csc^2(x) 
$$
</td>
<td style="vertical-align: top;">

$$
\dfrac{d}{dx} \arcsin\left(\dfrac{x}{a}\right) = \dfrac{a}{\sqrt{a - x^2}} \\[0.3cm]
\dfrac{d}{dx} \arccos\left(\dfrac{x}{a}\right) = \dfrac{-a}{\sqrt{a - x^2}} \\[0.3cm]
\dfrac{d}{dx} \arctan\left(\dfrac{x}{a}\right) = \dfrac{a}{a^2 + x^2} 
$$
</td>
<td style="vertical-align: top;">

$$
\dfrac{d}{dx} \operatorname{arcsec}\left(\dfrac{x}{a}\right) = \dfrac{a}{|x|\sqrt{x^2 - a}} \\[0.3cm]
\dfrac{d}{dx} \operatorname{arccsc}\left(\dfrac{x}{a}\right) = \dfrac{-a}{|x|\sqrt{x^2 - a}} \\[0.3cm]
\dfrac{d}{dx} \operatorname{arccot}\left(\dfrac{x}{a}\right) = \dfrac{-a}{a + x^2}
$$
</td>
</tr>
</table>

<h4 style="margin: 0;">Techniques of Integration</h4>
<!-- The blank rows in each <td> block, and lack of indents inside the table HTML, are so the KaTeX parser doesn't break while parsing formulas inside the $$ signs, as discovered through trial and error. -->
<table style="width: 100%; text-align: left;">
<tr>
<td style="vertical-align: top;">

$$
\int u \, dv = uv \Big|_a^b - \int v \, du
$$
</td>
<td style="vertical-align: top;">

$$

$$
</td>
<td style="vertical-align: top;">

$$

$$
</td>
</tr>
</table>

<h4 style="margin: 0;">2D Conics (swap x and y if major axis is flipped)</h4>
<h3 style="margin: 0;">Should I keep it as a and b and just define the foci/vertices for ellipses/hyperbolas independently?</h3>
<h3 style="margin: 0;">Ellipses need asymptotes anyway. Also, I believe my hyperbola definition does not match the textbook (I had thought I refined it such that it was valid, but it does not appear to be correct... maybe it was only correct on that particular problem and I was too exhausted/high at the time to attempt another).</h3>
<h3 style="margin: 0;">Also, chapter 10.6 also uses a and b.</h3>
<!-- The blank rows in each <td> block, and lack of indents inside the table HTML, are so the KaTeX parser doesn't break while parsing formulas inside the $$ signs, as discovered through trial and error. -->
<table style="width: 100%; text-align: left;">
<tr>
<td style="vertical-align: top;">

$$
Ellipse: \dfrac{(x-x_0)^2}{a^2} + \dfrac{(y-y_0)^2}{b^2} = \dfrac{(x-x_0)^2}{\left(\dfrac{Δv}{2}\right)^2} + \dfrac{(y-y_0)^2}{\left(\dfrac{Δv}{2}\right)^2 - \left(\dfrac{Δf}{2}\right)^2} = 1 \\[0.3cm]
Hyperbola: \dfrac{(x-x_0)^2}{a^2} + \dfrac{(y-y_0)^2}{b^2} = \dfrac{(x-x_0)^2}{2(Δv)^2} + \dfrac{(y-y_0)^2}{\left(\dfrac{Δf}{2}\right)^2 - 2(Δv)^2} = 1 \\[0.3cm]
Foci: \left(x_o±\dfrac{Δf}{2}, y_0\right)
Vertices: \left(x_o±\dfrac{Δv}{2}, y_0\right) \\[0.3cm]

$$
</td>
<td style="vertical-align: top;">

$$ 
(Ellipse) \hspace{0.55cm}a ≥ b > 0 \\[0.3cm]
Parabola: (y-y_0)=a(x-x_0)^2=\dfrac{(x-x_0)^2}{4p} \\[0.3cm]
Focus: (x_0, y_0 + p) \\[0.3cm]
Directrix: y = y_0 - p
$$
</td>
</tr>
</table>
<table>
<tr>
<td style="vertical-align: top;">

$$
Quadratic formula: x = \frac {-b \pm \sqrt{b^2 -4ac}} {2a}
$$
</table>
</td>
</tr>
</div>