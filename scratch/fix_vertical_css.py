import re

def fix_css(path):
    with open(path, 'r') as f:
        content = f.read()

    # The current responsive block might look like:
    # @media(max-width:900px) { ... .price-grid { min-width: 600px; grid-template-columns: repeat(7, 1fr) ... }
    # Or just default structure. Let's strictly replace the .price-grid block inside @media(max-width:900px).
    
    # Let's locate the @media(max-width:900px){ block and rewrite the .price-grid part inside it.
    # To be safe, let's append a more specific media query at the very end of the CSS <head> block
    
    vertical_css = """
    /* MOBILE VERTICAL PRICE GRID */
    @media(max-width:900px) {
      .tarifs-sec .ct, .tarifs-sec .rv { overflow-x: visible !important; padding-bottom: 0 !important; }
      .price-grid {
        display: grid !important;
        grid-template-columns: 1fr 1fr 1fr !important;
        grid-template-rows: repeat(7, auto) !important;
        grid-auto-flow: column !important;
        min-width: unset !important;
        gap: 0 !important;
        border: 1px solid rgba(255,255,255,.1) !important;
      }
      .pg-head { border-right: none !important; border-bottom: 1px solid rgba(255,255,255,.07) !important; display:flex !important; align-items:center !important; justify-content:flex-start !important; padding: 12px 16px !important; text-align: left !important; }
      .pg-cell { border-right: none !important; border-bottom: 1px solid rgba(255,255,255,.07) !important; border-top:none !important; display:flex !important; align-items:center !important; flex-direction:column !important; justify-content:center !important; padding: 12px 8px !important; }
      .pg-ppd { border-right: none !important; border-bottom: 1px solid rgba(255,255,255,.07) !important; border-top:none !important; padding: 12px 8px !important; display:flex !important; align-items:center !important; justify-content:center !important; }
      .pg-head span { margin-left: 6px; }
      
      /* Option Grid Mobile */
      .opts-grid { grid-template-columns: 1fr !important; }
    }
  </style>
"""
    
    # Replace the existing </style> with our appended CSS overrides
    if "/* MOBILE VERTICAL PRICE GRID */" not in content:
        content = content.replace("</style>", vertical_css)
        with open(path, 'w') as f:
            f.write(content)

fix_css('/home/gregory/Voilier/site/index.html')
fix_css('/home/gregory/Voilier/site/en/index.html')
fix_css('/home/gregory/Voilier/site/de/index.html')
print("Vertical CSS added to all files")
