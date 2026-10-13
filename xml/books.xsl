<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <title>Book Catalog</title>
      </head>
      <body>
        <h2>Book Catalog</h2>
        <table border="1">
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Price</th>
          </tr>

          <xsl:for-each select="catalog/book">
            <tr>
              <td><xsl:value-of select="title"/></td>
              <td><xsl:value-of select="author"/></td>
              <td>Rs. <xsl:value-of select="price"/></td>
            </tr>
          </xsl:for-each>

        </table>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>


//For CSS formatting, keep this line in books.xml:
<?xml-stylesheet type="text/css" href="books.css"?>


For XSLT formatting, replace it with:
<?xml-stylesheet type="text/xsl" href="books.xsl"?>