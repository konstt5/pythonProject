
import pygame
import os

pygame.init()
pygame.display.set_mode((800, 600), pygame.RESIZABLE)

### Style Costants ###
VECTORIAL = 0
GRAPHICAL = 1

darkColors = {'BGColor': (60, 63, 65),
              'TextColor': (175, 177, 179),
              'TextColorDisabled': (119, 119, 119),
              'BorderColor': (94, 96, 96),
              'GreenColor': (73, 156, 84),
              'GreyColor': (89, 89, 89),
              'BlueColor': (62, 134, 160),
              'FocusColor': (76, 80, 82)}

### Default Styles ###
path = os.path.dirname(os.path.abspath(__file__))
artpath = os.path.join(os.path.abspath("."), "art")

#Default font
defaultFont = pygame.font.Font(os.path.join(path, "font.otf"), 14)
titleFont = pygame.font.Font(os.path.join(path, "font.otf"), 14)
titleFont.set_bold(True)

### Label Style ###

defaultLabelStyle = {'font': defaultFont,
                     'font-color': (0, 0, 0),
                     'bg-color': (0, 0, 0, 0),
                     'border-width': 0,
                     'border-color': (0, 0, 0),
                     'wordwrap': True,
                     'antialias': True}

darkLabelStyle = {'font': defaultFont,
                     'font-color': darkColors['TextColor'],
                     'bg-color': (0, 0, 0, 0),
                     'border-width': 0,
                     'border-color': darkColors['BorderColor'],
                     'wordwrap': True,
                     'antialias': True}

#### Button Style ###

defaultButtonStyle = {'font': defaultFont,
                      'antialias': True,

                      'font-color': (255, 255, 255),
                      'font-color-over': (0, 0, 0),
                      'font-color-down': (100, 100, 100),
                      'font-color-disabled': (100, 100, 100),

                      'appearence': VECTORIAL,

                      'border-width': 1,
                      'border-width-focus': 1,

                      'border-color': (0, 0, 0),
                      'bg-color': (0, 0, 0, 200),

                      'border-color-over': (0, 0, 0),
                      'bg-color-over': (100, 100, 100, 200),

                      'border-color-down': (0, 0, 0),
                      'bg-color-down': (0, 0, 0, 250),

                      'border-color-disabled': (0, 0, 0),
                      'bg-color-disabled': (90, 90, 90),

                      'border-color-focus': (0, 0, 0),
                      'focus-color': (0, 0, 0, 100)
                      }

darkButtonStyle = {'font': defaultFont,
                      'antialias': True,
                      'autosize': True,

                      'font-color': darkColors['TextColor'],
                      'font-color-over': darkColors['TextColor'],
                      'font-color-down': darkColors['TextColor'],
                      'font-color-disabled': darkColors['TextColorDisabled'],

                      'appearence': VECTORIAL,

                      'border-width': 1,
                      'border-width-focus': 3,

                      'border-color': darkColors['BorderColor'],
                      'border-color-over': darkColors['BorderColor'],
                      'border-color-down': darkColors['BorderColor'],
                      'border-color-disabled': darkColors['BorderColor'],
                      'border-color-focus': darkColors['BlueColor'],

                      'bg-color': darkColors['BGColor'],
                      'bg-color-over': darkColors['FocusColor'],
                      'bg-color-down': (92, 97, 100),
                      'bg-color-disabled': darkColors['BGColor'],

                      'focus-color': darkColors['FocusColor']
                   }

graphicButtonStyleTemplate = {'font': defaultFont,
                              'antialias': True,
                              
                              'font-color':(0,0,0),
                              'font-color-over': (0,0,0),
                              'font-color-down': (0,0,0),
                              'font-color-disabled': (0,0,0), 
                              
                              'appearence': GRAPHICAL,
                              
                              'skin': None,
                              'widths-normal': (4,1,4),
                              'widths-over': (4,1,4),
                              'widths-down': (4,1,4),
                              'widths-disabled': (4,1,4),
                              'widths-focused': (0,0,0)
                              }

winButtonStyle = {'font': defaultFont,
                      'antialias': True,
                      'autosize': True,

                      'appearence': GRAPHICAL,

                      'font-color': (0, 0, 0),
                      'font-color-over': (0, 0, 0),
                      'font-color-down': (0, 0, 0),

                      'font-color-disabled': (0, 0, 0),

                      'skin': pygame.image.load(os.path.join(artpath, "button.png")).convert_alpha(),
                      'widths-normal': (4, 1, 4),
                      'widths-over': (4, 1, 4),
                      'widths-down': (4, 1, 4),
                      'widths-disabled': (4, 1, 4),
                      'widths-focused': (6, 2, 6)
                      }

windowButtonsStyle = defaultButtonStyle.copy()
windowButtonsStyle['autosize'] = False

defaultWindowStyle = {'font': titleFont,
                      'font-color': (255,255,255),
                      'offset-top-left': (7,37),
                      'offset-bottom-right': (7,7),
                      'title-position': (10,8),
                      
                      'appearence': VECTORIAL,
                      
                      'bg-color': (0,0,0,150),
                      'border-width': 1,
                      'border-color': (30,50,100),
                      'header-color': (0,0,50,100),
                      'header-offset': 5,
                      'header-height': 25,
                      'close-button-vectorial-style':  windowButtonsStyle,
                      'shade-button-vectorial-style':  windowButtonsStyle,
                      }



graphicWindowStyleTemplate = {'font': titleFont,
                      'font-color': (255,255,255),
                      'offset-top-left': (7,37),
                      'offset-bottom-right': (7,7),
                      'title-position': (10,8),
                      
                      'appearence': GRAPHICAL,
                      
                      'border-offset-top-left': (0,0),
                      'border-offset-bottom-right': (0,0),

                      'image-top-left': None,
                      'image-top': None,
                      'image-top-right': None,
                      'image-right': None,
                      'image-bottom-right': None,
                      'image-bottom': None,
                      'image-bottom-left': None,
                      'image-left': None,
                      
                      'close-button-skin':  None,
                      'shade-button-skin':  None,
                      
                      'close-button-offset': (5,5),
                      'shade-button-offset': (30,5),
                      'shade-button-only-offset': (5,5)
                      }

### Texbox styles ###

defaultTextBoxStyle = {'font': defaultFont,
                       'antialias': True,
                       'offset': (4, 4),

                       'font-color': (200, 200, 255),
                       'font-color-focus': (255, 255, 255),
                       'font-color-disabled': (0, 0, 0),

                       'appearence': VECTORIAL,

                       'border-color': (0, 0, 0),
                       'border-width': 1,
                       'bg-color': (55, 55, 55),

                       'border-color-focus': (0, 50, 50),
                       'border-width-focus': 1,
                       'bg-color-focus': (70, 70, 80),

                       'border-color-disabled': (0, 0, 0),
                       'bg-color-disabled': (90, 90, 90),
                       }

darkTextBoxStyle = {'font': defaultFont,
                       'antialias': True,
                       'offset': (4, 4),

                       'font-color': darkColors['TextColor'],
                       'font-color-focus': darkColors['TextColor'],
                       'font-color-disabled': darkColors['TextColorDisabled'],

                       'appearence': VECTORIAL,

                       'border-color': darkColors['BorderColor'],
                       'border-width': 1,
                       'bg-color': darkColors['BGColor'],

                       'border-color-focus': darkColors['BlueColor'],
                       'border-width-focus': 3,
                       'bg-color-focus': darkColors['FocusColor'],

                       'border-color-disabled': (0, 0, 0),
                       'bg-color-disabled': darkColors['BGColor'],
                       }

### Checkbox styles ###

defaultCheckBoxStyle = {'font': defaultFont,
                        'font-color': (0, 0, 0),
                        'font-color-disabled': (50, 50, 50),
                        'wordwrap': True,
                        'antialias': True,
                        'spacing': 4,

                        'appearence': VECTORIAL,

                        'box-width': 16,

                        'box-color': (50, 50, 50, 100),
                        'box-color-over': (150, 150, 150, 200),
                        'box-color-down': (50, 50, 50, 100),
                        'box-color-disabled': (10, 100, 100, 100),

                        'border-color': (0, 0, 0),
                        'border-color-over': (0, 0, 0),
                        'border-color-down': (0, 0, 0),
                        'border-color-disabled': (0, 0, 0),

                        'check-color': (255, 255, 255),
                        'check-color-over': (100, 100, 255),
                        'check-color-down': (5, 5, 5),
                        'check-color-disabled': (250, 250, 250)
                        }

darkCheckBoxStyle = {'font': defaultFont,
                        'font-color': darkColors['TextColor'],
                        'font-color-disabled': darkColors['TextColorDisabled'],
                        'wordwrap': True,
                        'antialias': True,
                        'spacing': 4,

                        'appearence': VECTORIAL,

                        'box-width': 16,

                        'box-color': darkColors['BGColor'],
                        'box-color-over': darkColors['FocusColor'],
                        'box-color-down': (92, 97, 100),
                        'box-color-disabled': darkColors['BGColor'],

                        'border-color': darkColors['BorderColor'],
                        'border-color-over': darkColors['BorderColor'],
                        'border-color-down': darkColors['BorderColor'],
                        'border-color-disabled': darkColors['BorderColor'],

                        'check-color': darkColors['GreenColor'],
                        'check-color-over': darkColors['GreenColor'],
                        'check-color-down': darkColors['GreenColor'],
                        'check-color-disabled': darkColors['GreyColor']
                        }

winCheckBoxStyle = {'font': defaultFont,
                        'font-color': (0, 0, 0),
                        'font-color-disabled': (50, 50, 50),
                        'wordwrap': True,
                        'antialias': True,
                        'spacing': 4,

                        'appearence': GRAPHICAL,

                        'skin': pygame.image.load(os.path.join(artpath, "checkbox.png")).convert_alpha(),

                        'box-width': 16,

                        'box-color': (50, 50, 50, 100),
                        'box-color-over': (150, 150, 150, 200),
                        'box-color-down': (50, 50, 50, 100),
                        'box-color-disabled': (10, 100, 100, 100),

                        'border-color': (0, 0, 0),
                        'border-color-over': (0, 0, 0),
                        'border-color-down': (0, 0, 0),
                        'border-color-disabled': (0, 0, 0),

                        'check-color': (255, 255, 255),
                        'check-color-over': (100, 100, 255),
                        'check-color-down': (5, 5, 5),
                        'check-color-disabled': (250, 250, 250)
                        }

### Themes ###

darkTheme = {'CheckBox': darkCheckBoxStyle,
             'Label': darkLabelStyle,
             'TextBox': darkTextBoxStyle,
             'ScrollBox': darkTextBoxStyle,
             'Button': darkButtonStyle,
             'BGColor': darkColors['BGColor']}

winTheme = {'CheckBox': winCheckBoxStyle,
            'Label': defaultLabelStyle,
            'TextBox': defaultTextBoxStyle,
            'ScrollBox': defaultTextBoxStyle,
            'Button': winButtonStyle}