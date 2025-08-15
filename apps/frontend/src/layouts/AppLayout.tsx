import { Outlet, Link } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { Card, CardHeader, CardTitle } from '@/components/ui/card'

export default function AppLayout() {
  return (
    <div className="min-h-screen bg-gray-100 p-4">
      {/* Header */}
      <header className="flex justify-between items-center bg-white shadow p-4 rounded">
        <h1 className="text-xl font-bold">My Store</h1>
        <nav className="space-x-2">
          <Link to="/login"><Button variant="outline">Login</Button></Link>
          <Link to="/register"><Button>Register</Button></Link>
        </nav>
      </header>

      {/* Main Content */}
      <main className="mt-6">
        <Card className="max-w-2xl mx-auto">
          <CardHeader>
            <CardTitle>Welcome</CardTitle>
          </CardHeader>
          <div className="p-4">
            <Outlet />
          </div>
        </Card>
      </main>
    </div>
  )
}

