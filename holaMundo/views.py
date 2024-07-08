from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
 return HttpResponse("""<a href="/">Home</a>
                     <a href="/about/">About</a>
                     <a href="/contact/">Contact</a>
                     <h1>Home</h1>
                     <p>Lorem ipsum dolor sit amet. Pellentesque mollis placerat turpis ut maximus.</p>""")
def about(request):
 return HttpResponse("""<a href="/">Home</a>
                     <a href="/about/">About</a>
                     <a href="/contact/">Contact</a>
                     <h1>About</h1>
                     <p>Lorem ipsum dolor sit amet. Pellentesque mollis placerat turpis ut maximus.</p>""")
def contact(request):
 return HttpResponse("""<a href="/">Home</a>
                     <a href="/about/">About</a>
                     <a href="/contact/">Contact</a>
                     <h1>Contact</h1>
                     <form>
                        <fieldset>
                        <legend>Contact Us</legend>
                            <label>Subject:</label><br>
                            <input type="text"><br>
                            <label>Body:</body><br>
                            <textarea name="body" rows="5" cols="21"></textarea><br>
                            <label>Email:</label><br>
                            <input type="email"><br><br>
                            <input type="submit">
                        </fieldset>
                     </form>""")
 