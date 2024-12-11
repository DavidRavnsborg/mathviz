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

<h4 style="margin: 0;">Multivariable Calculus Derivatives/Integrals</h4>
<!-- The blank rows in each <td> block, and lack of indents inside the table HTML, are so the KaTeX parser doesn't break while parsing formulas inside the $$ signs, as discovered through trial and error. -->
<table style="width: 100%; text-align: left;">
<tr>
<td style="vertical-align: top;">

$$
L = \int_{α}^{β} \sqrt{\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2} \ dt = \int_{a}^{b} \sqrt{1 + \left(\dfrac{dy}{dx}\right)^2} \ dx = \int_{A}^{B} \sqrt{r^2 + \left(\dfrac{dr}{dθ}\right)^2} \ dθ \\[0.3cm]

T(t) = \dfrac{r'(t)}{\left\Vert r'(t) \right\Vert} \hspace{5pt} K = \left\Vert T'(s) \right\Vert = \dfrac{\left\Vert T'(t) \right\Vert}{\left\Vert r'(t) \right\Vert} = \dfrac{\left\Vert r'(t) \times r''(t) \right\Vert}{\left\Vert r'(t) \right\Vert ^3} = \dfrac{\left\vert f''(x) \right\vert}{(1 + f'(x)^2)^\frac{3}{2}} \\[0.3cm]

N(t) = \dfrac{T'(t)}{\Vert T'(t) \Vert} \hspace{5pt} B(t) = T(t) \times N(t) \hspace{5pt} h_{max} = \dfrac{v_0^2}{2g} = -\dfrac{g}{2}t^2+v_0t+h_0\\[0.3cm]

$$
</td>
<td style="vertical-align: top;">

$$
A = \int_{α}^{β} y(t)x'(t) dt = \int_{a}^{b} y dx = \int_{A}^{B} \dfrac{1}{2}r^2 dθ \\[0.3cm]

\dfrac{d^2y}{dx^2} = \dfrac{d}{dx} \left(\dfrac{dy}{dx} \right) = \dfrac{\dfrac{d}{dt} \left(\dfrac{dy}{dx} \right)}{\dfrac{dx}{dt}} \\[0.3cm]
a = -\dfrac{GMm}{r^3}r = -\dfrac{GMm}{r^2}u
$$
</td>
</tr>
</table>

<h4 style="margin: 0;">Second Derivative Test</h4>
<table style="width: 100%; text-align: left;">
<tr style="text-align: left;">
<td style="vertical-align: top;">

$$
D(a,b) = f_{xx}(a,b)f_{yy}(a,b) - [f_{xy}(a,b)^2] \\[0.3cm]
Min:	D > 0 and f_{xx}(a,b) > 0 \\[0.3cm]
Max:	D > 0 and f_{xx}(a,b) < 0 \\[0.3cm]
Saddle: D < 0 \\[0.3cm]
Inconclusive: D = 0

$$
</td>
</tr>
</table>

<table style="width: 100%; text-align: left;">
<tr>
<td style="vertical-align: top;">

</td>
<td style="vertical-align: top;">
Ellipse
</td>
<td style="vertical-align: top;">
Parabola
</td>
<td style="vertical-align: top;">
Hyperbola
</td>
</tr>
<tr>
<td style="vertical-align: top;">
Formulae
</td>
<td style="vertical-align: top;">

$$ 
\dfrac{(x-h)^2}{a^2} + \dfrac{(y-k)^2}{b^2} = 1 \\[0.3cm]
$$
</td>
<td style="vertical-align: top;">

$$
(y-k)^2=4p(x-h) \\[0.3cm]
$$
</td>
<td style="vertical-align: top;">

$$
\dfrac{(x-h)^2}{a^2} - \dfrac{(y-k)^2}{b^2} = 1 \\[0.3cm]
$$
</td>
</tr>
<tr>
<td style="vertical-align: top;">
Foci
</td>
<td style="vertical-align: top;">

$$
(h±c, k), \hspace{5pt} a^2 - b^2 = c^2
$$
</td>
<td style="vertical-align: top;">

$$
(h+p, k), \hspace{5pt} p=-d
$$
</td>
<td style="vertical-align: top;">

$$
(h±c, k), \hspace{5pt} a^2 + b^2 = c^2
$$
</td>
</tr>
<td style="vertical-align: top;">
Vertices
</td>
<td style="vertical-align: top;">

$$
(h±a, k)
$$
</td>
<td style="vertical-align: top;">

$$
(h, k)
$$
</td>
<td style="vertical-align: top;">

$$
(h±a, k)
$$
</td>
</tr>
</table>

<table style="width: 100%; text-align: left;">
<tr>

$$
Polar form (opens left/right/down/up): r = \dfrac{ed}{1 + ecos(θ)} \hspace{5pt} / \hspace{5pt} r = \dfrac{ed}{1 - ecos(θ)} \hspace{5pt} / \hspace{5pt} r = \dfrac{ed}{1 + esin(θ)} \hspace{5pt} / \hspace{5pt} r = \dfrac{ed}{1 - esin(θ)}
$$
</tr>
</table>
<table>
<tr>
<td style="vertical-align: top;">

$$
Eccentricity: \dfrac{c}{a} = e = \dfrac{a}{d}
$$
</td>
<td style="vertical-align: top;">

$$
h = -\dfrac{e^2d}{1-e^2}
$$
</td>
<td style="vertical-align: top;">

$$
a^2 = \dfrac{e^2d^2}{(1-e^2)^2}
$$
</td>
<td style="vertical-align: top;">

$$
b^2 = \dfrac{e^2d^2}{1-e^2}
$$
</td>
<td style="vertical-align: top;">

NOTE: This $b^2 $ is the negative of {b^2} in the hyperbola formula above, since it naturally gives a negative when e>1.
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