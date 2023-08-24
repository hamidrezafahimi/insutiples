

### undefined reference to ...

As I know, this is the most bothering error in cpp. There are a couple of reasons for that:

1. The most simple reason is that: A function (or whatever) is declared (like in a header file) and not defined (like in a library file).

2. If the reason 1 is not true, another probable reason is that: The library file in which function (or whatever) is defined is not linked correctly to the header file by cmake. Go and kick cmake's ass so that it works fine.

3. Oh ...! I have spent lots of time in this situation! Let me give you a pointer. There is another probable reason for this, if 1 and 2 are not true. That is: Assume that you have made an executable (with an `int main() {}`) inside it. If you declare and define something in your header files and libraries, and do not implement it runtime, (i. e. call it in the nested execution inside your `main` function). Then it's possible to face this error. To fix, you should call the defined function in your `main` function. 


### undefined reference to `vtable for <class-A>'

Inside the class A, you've declared a non-pure virtual function which is not defined in the library.


### cannot declare variable 'dobj' to be of abstract type 'D'

- D is an abstract class (has pure virtual function inside it)

- D inherits an abstract class A in which there is a function for which no body is defined in the current branch of inheritance from A to D.