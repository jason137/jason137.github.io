-- Give each standalone image a caption-free figure that links to the full-size
-- sheet in a new tab, and lazy-load it. (Pandoc only makes figures from captioned images.)
function Para(para)
  if #para.content ~= 1 or para.content[1].t ~= "Image" then return nil end
  local img = para.content[1]
  img.attributes.loading = "lazy"
  local link = pandoc.Link({img}, img.src, "", {target = "_blank", rel = "noopener"})
  return pandoc.Figure(pandoc.Plain({link}), {long = {}})
end
