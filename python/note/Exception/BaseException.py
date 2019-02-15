BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning


###########################################################################
|Exception Name|Description|
|BaseException|Root class for all exceptions|
|   SystemExit|Request termination of Python interpreter|
|KeyboardInterrupt|User interrupted execution (usually by pressing Ctrl+C)|
|Exception|Root class for regular exceptions|
|   StopIteration|Iteration has no further values|
|   GeneratorExit|Exception sent to generator to tell it to quit|
|   SystemExit|Request termination of Python interpreter|
|   StandardError|Base class for all standard built-in exceptions|
|       ArithmeticError|Base class for all numeric calculation errors|
|           FloatingPointError|Error in floating point calculation|
|           OverflowError|Calculation exceeded maximum limit for numerical type|
|           ZeroDivisionError|Division (or modulus) by zero error (all numeric types)|
|       AssertionError|Failure of assert statement|
|       AttributeError|No such object attribute|
|       EOFError|End-of-file marker reached without input from built-in|
|       EnvironmentError|Base class for operating system environment errors|
|           IOError|Failure of input/output operation|
|           OSError|Operating system error|
|               WindowsError|MS Windows system call failure|
|               ImportError|Failure to import module or object|
|               KeyboardInterrupt|User interrupted execution (usually by pressing Ctrl+C)|
|           LookupError|Base class for invalid data lookup errors|
|               IndexError|No such index in sequence|
|               KeyError|No such key in mapping|
|           MemoryError|Out-of-memory error (non-fatal to Python interpreter)|
|           NameError|Undeclared/uninitialized object(non-attribute)|
|               UnboundLocalError|Access of an uninitialized local variable|
|           ReferenceError|Weak reference tried to access a garbage collected object|
|           RuntimeError|Generic default error during execution|
|               NotImplementedError|Unimplemented method|
|           SyntaxError|Error in Python syntax|
|               IndentationError|Improper indentation|
|                   TabErrorg|Improper mixture of TABs and spaces|
|           SystemError|Generic interpreter system error|
|           TypeError|Invalid operation for type|
|           ValueError|Invalid argument given|
|               UnicodeError|Unicode-related error|
|                   UnicodeDecodeError|Unicode error during decoding|
|                   UnicodeEncodeError|Unicode error during encoding|
|                   UnicodeTranslate Error|Unicode error during translation|
|       Warning|Root class for all warnings|
|           DeprecationWarning|Warning about deprecated features|
|           FutureWarning|Warning about constructs that will change semantically in the future|
|           OverflowWarning|Old warning for auto-long upgrade|
|           PendingDeprecation Warning|Warning about features that will be deprecated in the future|
|           RuntimeWarning|Warning about dubious runtime behavior|
|           SyntaxWarning|Warning about dubious syntax|
|           UserWarning|Warning generated by user code|